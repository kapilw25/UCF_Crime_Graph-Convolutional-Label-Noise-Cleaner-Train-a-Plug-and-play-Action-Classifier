```bash
tree -P '*.*' --noreport
```

.
├── Graph Convolutional Label Noise Cleaner- Train a Plug-and-play Action Classifier for Anomaly Detection.pdf
├── README.md
├── ShanghaiTech_new_split
│   ├── SH_Test.txt
│   └── SH_Train.txt
├── feature_extraction
│   ├── extract_c3d
│   │   ├── extract_c3d_all.py
│   │   ├── pyActionRecog
│   │   │   ├── MatInfo.py
│   │   │   ├── __init__.py
│   │   │   ├── action_caffe.py
│   │   │   ├── action_parrots.py
│   │   │   ├── anet_db.py
│   │   │   ├── benchmark_db.py
│   │   │   └── utils
│   │   │       ├── io.py
│   │   │       ├── metrics.py
│   │   │       └── video_funcs.py
│   │   └── ucf_crimes
│   │       ├── c3d_deploy.prototxt
│   │       └── kinetics_c3d_deploy.prototxt
│   ├── extract_tsn
│   │   ├── kinetics_extract_flow.py
│   │   ├── kinetics_extract_rgb.py
│   │   ├── pyActionRecog
│   │   │   ├── MatInfo.py
│   │   │   ├── __init__.py
│   │   │   ├── action_caffe.py
│   │   │   ├── action_parrots.py
│   │   │   ├── anet_db.py
│   │   │   ├── benchmark_db.py
│   │   │   └── utils
│   │   │       ├── io.py
│   │   │       ├── metrics.py
│   │   │       └── video_funcs.py
│   │   └── ucf_crimes
│   │       ├── bn_inception_flow_deploy.prototxt
│   │       ├── bn_inception_rgb_deploy.prototxt
│   │       ├── spatial_untrimmednet_hard_bn_inception_deploy.prototxt
│   │       └── temporal_untrimmednet_hard_bn_inception_deploy.prototxt
│   └── readme.md
└── pygcn
    ├── dataset.py
    ├── dataset_test.py
    ├── experiment_c3d.py
    ├── experiment_flow.py
    ├── experiment_rgb.py
    ├── layers.py
    ├── make_soft_label_c3d_high_conf.py
    ├── make_soft_label_flow_high_conf.py
    ├── make_soft_label_rgb_high_conf.py
    ├── models.py
    ├── train.py
    ├── ucf_crime_train.pkl
    ├── utils.py
    └── visualize_c3d_prediction.py

# GCN-Anomaly-Detection

[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)


Our source codes for the following paper at CVPR 2019:

## Graph Convolutional Label Noise Cleaner: Train a Plug-and-play Action Classifier for Anomaly Detection

```
@inproceedings{adgcn_cvpr19,
  author    = {Jia-Xing Zhong and
	       Nannan Li and
               Weijie Kong and
               Shan Liu and
               Thomas H. Li and
               Ge Li},
  title     = {Graph Convolutional Label Noise Cleaner: Train a Plug-and-play Action Classifier for Anomaly Detection},
  booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year      = {2019}
}
```

Our codes for feature extraction have been released! The training codes are also available as in the folder pygcn. 
