import sys

import caffe
from caffe.io import oversample
import numpy as np
from .utils.io import fast_list2arr, flow_stack_oversample, c3d_flow_stack_oversample, c3d_rgb_stack_oversample
import cv2


class CaffeNet(object):
    def __init__(self, net_proto, net_weights, device_id, input_size=None):
        caffe.set_mode_gpu()
        caffe.set_device(device_id)
        self._net = caffe.Net(net_proto, net_weights, caffe.TEST)

        input_shape = self._net.blobs['data'].data.shape

        if input_size is not None:
            input_shape = input_shape[:2] + input_size

        transformer = caffe.io.Transformer({'data': input_shape})

        if self._net.blobs['data'].data.shape[1] == 3:
            # transformer.set_transpose('data', (0, 3, 1, 2))  # move image channels to outermost dimension
            # transformer.set_mean('data', np.array([104, 117, 123]))  # subtract the dataset-mean value in each channel
            pass
        else:
            pass  # non RGB data need not use transformer

        self._transformer = transformer

        self._sample_shape = self._net.blobs['data'].data.shape

    def predict_single_frame(self, frame, score_name, over_sample=True, multiscale=None, frame_size=None,
                             attention_name=None):

        if frame_size is not None:
            frame = [cv2.resize(x, frame_size) for x in frame]

        if over_sample:
            if multiscale is None:
                os_frame = oversample(frame, (self._sample_shape[2], self._sample_shape[3]))
            else:
                os_frame = []
                for scale in multiscale:
                    resized_frame = [cv2.resize(x, (0, 0), fx=1.0 / scale, fy=1.0 / scale) for x in frame]
                    os_frame.extend(oversample(resized_frame, (self._sample_shape[2], self._sample_shape[3])))
        else:
            os_frame = fast_list2arr(frame)
        # data = fast_list2arr([self._transformer.preprocess('data', x) for x in os_frame])
        data = os_frame - [104.0, 117.0, 123.0]
        data = data.transpose(0, 3, 1, 2)
        self._net.blobs['data'].reshape(*data.shape)
        self._net.reshape()
        if attention_name is None:
            out = self._net.forward(blobs=[score_name, ], data=data)
            return out[score_name].copy()
        else:
            out = self._net.forward(blobs=[score_name, attention_name], data=data)
            return out[score_name].copy(), out[attention_name].copy()

    def predict_single_flow_stack(self, frame, score_name, over_sample=True, frame_size=None, attention_name=None):

        if frame_size is not None:
            frame = fast_list2arr([cv2.resize(x, frame_size) for x in frame])
        else:
            frame = fast_list2arr(frame)

        if over_sample:
            os_frame = flow_stack_oversample(frame, (self._sample_shape[2], self._sample_shape[3]))
        else:
            os_frame = fast_list2arr([frame])

        data = os_frame - np.float32(128.0)

        self._net.blobs['data'].reshape(*data.shape)
        self._net.reshape()
        if attention_name is None:
            out = self._net.forward(blobs=[score_name, ], data=data)
            return out[score_name].copy()
        else:
            out = self._net.forward(blobs=[score_name, attention_name], data=data)
            return out[score_name].copy(), out[attention_name].copy()

    def predict_single_c3d_rgb_stack(self, frame, score_name, over_sample=True, frame_size=None):

        if frame_size is not None:
            frame = fast_list2arr([cv2.resize(x, frame_size) for x in frame])
        else:
            frame = fast_list2arr(frame)

        if over_sample:
            os_frame = c3d_rgb_stack_oversample(frame, (self._sample_shape[3], self._sample_shape[4]))
        else:
            os_frame = fast_list2arr([frame])

        data = os_frame - np.float32([104.0, 117.0, 123.0]);
        data = np.transpose(data, [0, 4, 1, 2, 3])

        self._net.blobs['data'].data[...] = data.copy()
        self._net.forward()
        out = self._net.blobs[score_name].data.copy()
        return out.copy()

    def predict_single_c3d_flow_stack(self, frame, score_name, over_sample=True, frame_size=None):

        if frame_size is not None:
            frame = fast_list2arr([cv2.resize(x, frame_size) for x in frame])
        else:
            frame = fast_list2arr(frame)

        if over_sample:
            os_frame = c3d_flow_stack_oversample(frame, (self._sample_shape[3], self._sample_shape[4]))
        else:
            os_frame = fast_list2arr([frame])

        data = os_frame - np.float32(128.0);
        data = np.transpose(data, [0, 4, 1, 2, 3])

        self._net.blobs['data'].data[...] = data.copy()
        self._net.forward()
        out = self._net.blobs[score_name].data.copy()
        return out.copy()
