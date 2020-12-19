hparams = {'input_size': (512, 512, 3),
           'batch_size': 4,
           'content_weight': 1e-5, # 1e-5,
           'style_weight': 6e-9, # 4e-9,
           'learning_rate': 0.001,
           'test_size': (1024, 1024, 3),
           'residual_filters': 128,
           'residual_layers': 5,
           'initializer': 'glorot_normal',
           'style_layers': ['block1_conv2',
                            'block2_conv2',
                            'block3_conv3',
                            'block4_conv3']
}
