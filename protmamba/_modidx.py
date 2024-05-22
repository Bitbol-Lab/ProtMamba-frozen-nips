# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/protmamba',
                'doc_host': 'https://damiano-sg.github.io',
                'git_url': 'https://github.com/damiano-sg/protmamba',
                'lib_path': 'protmamba'},
  'syms': { 'protmamba.core': {'protmamba.core.run': ('core.html#run', 'protmamba/core.py')},
            'protmamba.dataloaders': { 'protmamba.dataloaders.DataCollatorForUniclust30Dataset': ( 'dataloaders.html#datacollatorforuniclust30dataset',
                                                                                                   'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.DataCollatorForUniclust30Dataset.__call__': ( 'dataloaders.html#datacollatorforuniclust30dataset.__call__',
                                                                                                            'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset': ( 'dataloaders.html#uniclust30_dataset',
                                                                                     'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.__getitem__': ( 'dataloaders.html#uniclust30_dataset.__getitem__',
                                                                                                 'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.__init__': ( 'dataloaders.html#uniclust30_dataset.__init__',
                                                                                              'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.__len__': ( 'dataloaders.html#uniclust30_dataset.__len__',
                                                                                             'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.get_index_start_of_sequences': ( 'dataloaders.html#uniclust30_dataset.get_index_start_of_sequences',
                                                                                                                  'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.get_sequences': ( 'dataloaders.html#uniclust30_dataset.get_sequences',
                                                                                                   'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.reverse_sequences': ( 'dataloaders.html#uniclust30_dataset.reverse_sequences',
                                                                                                       'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.Uniclust30_Dataset.sample_sequences': ( 'dataloaders.html#uniclust30_dataset.sample_sequences',
                                                                                                      'protmamba/dataloaders.py'),
                                       'protmamba.dataloaders.make_dataloader': ( 'dataloaders.html#make_dataloader',
                                                                                  'protmamba/dataloaders.py')},
            'protmamba.fim': { 'protmamba.fim.AbstractFIM': ('fim.html#abstractfim', 'protmamba/fim.py'),
                               'protmamba.fim.AbstractFIM.__init__': ('fim.html#abstractfim.__init__', 'protmamba/fim.py'),
                               'protmamba.fim.AbstractFIM.apply': ('fim.html#abstractfim.apply', 'protmamba/fim.py'),
                               'protmamba.fim.AbstractFIM.fim': ('fim.html#abstractfim.fim', 'protmamba/fim.py'),
                               'protmamba.fim.MultipleSpanFIM': ('fim.html#multiplespanfim', 'protmamba/fim.py'),
                               'protmamba.fim.MultipleSpanFIM.__init__': ('fim.html#multiplespanfim.__init__', 'protmamba/fim.py'),
                               'protmamba.fim.MultipleSpanFIM.fim': ('fim.html#multiplespanfim.fim', 'protmamba/fim.py'),
                               'protmamba.fim.MultipleSpanFIM.split_sequences': ( 'fim.html#multiplespanfim.split_sequences',
                                                                                  'protmamba/fim.py'),
                               'protmamba.fim.NoFIM': ('fim.html#nofim', 'protmamba/fim.py'),
                               'protmamba.fim.NoFIM.__init__': ('fim.html#nofim.__init__', 'protmamba/fim.py'),
                               'protmamba.fim.NoFIM.fim': ('fim.html#nofim.fim', 'protmamba/fim.py'),
                               'protmamba.fim.SingleSpanFIM': ('fim.html#singlespanfim', 'protmamba/fim.py'),
                               'protmamba.fim.SingleSpanFIM.__init__': ('fim.html#singlespanfim.__init__', 'protmamba/fim.py'),
                               'protmamba.fim.SingleSpanFIM.fim': ('fim.html#singlespanfim.fim', 'protmamba/fim.py')},
            'protmamba.modules': { 'protmamba.modules.CheckpointedModule': ('modules.html#checkpointedmodule', 'protmamba/modules.py'),
                                   'protmamba.modules.CheckpointedModule.__init__': ( 'modules.html#checkpointedmodule.__init__',
                                                                                      'protmamba/modules.py'),
                                   'protmamba.modules.CheckpointedModule.forward': ( 'modules.html#checkpointedmodule.forward',
                                                                                     'protmamba/modules.py'),
                                   'protmamba.modules.GenerationMixinSafe': ('modules.html#generationmixinsafe', 'protmamba/modules.py'),
                                   'protmamba.modules.GenerationMixinSafe.generate': ( 'modules.html#generationmixinsafe.generate',
                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.MambaConfig': ('modules.html#mambaconfig', 'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe': ('modules.html#mambalmheadmodelsafe', 'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.__init__': ( 'modules.html#mambalmheadmodelsafe.__init__',
                                                                                        'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.allocate_inference_cache': ( 'modules.html#mambalmheadmodelsafe.allocate_inference_cache',
                                                                                                        'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.clip_grad_norm_': ( 'modules.html#mambalmheadmodelsafe.clip_grad_norm_',
                                                                                               'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.forward': ( 'modules.html#mambalmheadmodelsafe.forward',
                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.from_pretrained': ( 'modules.html#mambalmheadmodelsafe.from_pretrained',
                                                                                               'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.protected_forward': ( 'modules.html#mambalmheadmodelsafe.protected_forward',
                                                                                                 'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.save_pretrained': ( 'modules.html#mambalmheadmodelsafe.save_pretrained',
                                                                                               'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelSafe.tie_weights': ( 'modules.html#mambalmheadmodelsafe.tie_weights',
                                                                                           'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids': ( 'modules.html#mambalmheadmodelwith2dposids',
                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.__init__': ( 'modules.html#mambalmheadmodelwith2dposids.__init__',
                                                                                                'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.allocate_inference_cache': ( 'modules.html#mambalmheadmodelwith2dposids.allocate_inference_cache',
                                                                                                                'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.forward': ( 'modules.html#mambalmheadmodelwith2dposids.forward',
                                                                                               'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.from_pretrained': ( 'modules.html#mambalmheadmodelwith2dposids.from_pretrained',
                                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.protected_forward': ( 'modules.html#mambalmheadmodelwith2dposids.protected_forward',
                                                                                                         'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.save_pretrained': ( 'modules.html#mambalmheadmodelwith2dposids.save_pretrained',
                                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwith2DPosids.tie_weights': ( 'modules.html#mambalmheadmodelwith2dposids.tie_weights',
                                                                                                   'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids': ( 'modules.html#mambalmheadmodelwithposids',
                                                                                     'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.__init__': ( 'modules.html#mambalmheadmodelwithposids.__init__',
                                                                                              'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.allocate_inference_cache': ( 'modules.html#mambalmheadmodelwithposids.allocate_inference_cache',
                                                                                                              'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.forward': ( 'modules.html#mambalmheadmodelwithposids.forward',
                                                                                             'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.from_pretrained': ( 'modules.html#mambalmheadmodelwithposids.from_pretrained',
                                                                                                     'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.protected_forward': ( 'modules.html#mambalmheadmodelwithposids.protected_forward',
                                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.save_pretrained': ( 'modules.html#mambalmheadmodelwithposids.save_pretrained',
                                                                                                     'protmamba/modules.py'),
                                   'protmamba.modules.MambaLMHeadModelwithPosids.tie_weights': ( 'modules.html#mambalmheadmodelwithposids.tie_weights',
                                                                                                 'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelSafe': ('modules.html#mixermodelsafe', 'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelSafe.forward': ( 'modules.html#mixermodelsafe.forward',
                                                                                 'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWith2DPosids': ( 'modules.html#mixermodelwith2dposids',
                                                                                 'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWith2DPosids.__init__': ( 'modules.html#mixermodelwith2dposids.__init__',
                                                                                          'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWith2DPosids.allocate_inference_cache': ( 'modules.html#mixermodelwith2dposids.allocate_inference_cache',
                                                                                                          'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWith2DPosids.forward': ( 'modules.html#mixermodelwith2dposids.forward',
                                                                                         'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWithPosids': ('modules.html#mixermodelwithposids', 'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWithPosids.__init__': ( 'modules.html#mixermodelwithposids.__init__',
                                                                                        'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWithPosids.allocate_inference_cache': ( 'modules.html#mixermodelwithposids.allocate_inference_cache',
                                                                                                        'protmamba/modules.py'),
                                   'protmamba.modules.MixerModelWithPosids.forward': ( 'modules.html#mixermodelwithposids.forward',
                                                                                       'protmamba/modules.py'),
                                   'protmamba.modules.create_block': ('modules.html#create_block', 'protmamba/modules.py'),
                                   'protmamba.modules.decode_safe': ('modules.html#decode_safe', 'protmamba/modules.py'),
                                   'protmamba.modules.load_model': ('modules.html#load_model', 'protmamba/modules.py'),
                                   'protmamba.modules.sample_safe': ('modules.html#sample_safe', 'protmamba/modules.py')},
            'protmamba.trainer': { 'protmamba.trainer.EarlyStoppingCallback': ( 'trainer.html#earlystoppingcallback',
                                                                                'protmamba/trainer.py'),
                                   'protmamba.trainer.EarlyStoppingCallback.__init__': ( 'trainer.html#earlystoppingcallback.__init__',
                                                                                         'protmamba/trainer.py'),
                                   'protmamba.trainer.EarlyStoppingCallback.get_checkpoint_path': ( 'trainer.html#earlystoppingcallback.get_checkpoint_path',
                                                                                                    'protmamba/trainer.py'),
                                   'protmamba.trainer.EarlyStoppingCallback.on_evaluate': ( 'trainer.html#earlystoppingcallback.on_evaluate',
                                                                                            'protmamba/trainer.py'),
                                   'protmamba.trainer.EarlyStoppingCallback.on_train_begin': ( 'trainer.html#earlystoppingcallback.on_train_begin',
                                                                                               'protmamba/trainer.py'),
                                   'protmamba.trainer.MambaTrainer': ('trainer.html#mambatrainer', 'protmamba/trainer.py'),
                                   'protmamba.trainer.MambaTrainer.__init__': ( 'trainer.html#mambatrainer.__init__',
                                                                                'protmamba/trainer.py'),
                                   'protmamba.trainer.MambaTrainer.compute_loss': ( 'trainer.html#mambatrainer.compute_loss',
                                                                                    'protmamba/trainer.py'),
                                   'protmamba.trainer.MambaTrainer.save_model': ( 'trainer.html#mambatrainer.save_model',
                                                                                  'protmamba/trainer.py'),
                                   'protmamba.trainer.get_last_checkpoint': ('trainer.html#get_last_checkpoint', 'protmamba/trainer.py')},
            'protmamba.utils': { 'protmamba.utils.clean_sequence': ('utils.html#clean_sequence', 'protmamba/utils.py'),
                                 'protmamba.utils.compute_metrics': ('utils.html#compute_metrics', 'protmamba/utils.py'),
                                 'protmamba.utils.concatenate_loggings': ('utils.html#concatenate_loggings', 'protmamba/utils.py'),
                                 'protmamba.utils.decode_sequence': ('utils.html#decode_sequence', 'protmamba/utils.py'),
                                 'protmamba.utils.encode_sequence': ('utils.html#encode_sequence', 'protmamba/utils.py'),
                                 'protmamba.utils.filter_datapoints': ('utils.html#filter_datapoints', 'protmamba/utils.py'),
                                 'protmamba.utils.find_fim_indices': ('utils.html#find_fim_indices', 'protmamba/utils.py'),
                                 'protmamba.utils.generate_sequence': ('utils.html#generate_sequence', 'protmamba/utils.py'),
                                 'protmamba.utils.load_from_file': ('utils.html#load_from_file', 'protmamba/utils.py'),
                                 'protmamba.utils.load_tensorboard_data': ('utils.html#load_tensorboard_data', 'protmamba/utils.py'),
                                 'protmamba.utils.merge_loggings': ('utils.html#merge_loggings', 'protmamba/utils.py'),
                                 'protmamba.utils.prepare_dataset_for_fim_generation': ( 'utils.html#prepare_dataset_for_fim_generation',
                                                                                         'protmamba/utils.py'),
                                 'protmamba.utils.prepare_target': ('utils.html#prepare_target', 'protmamba/utils.py'),
                                 'protmamba.utils.prepare_tokens': ('utils.html#prepare_tokens', 'protmamba/utils.py'),
                                 'protmamba.utils.print_number_of_parameters': ( 'utils.html#print_number_of_parameters',
                                                                                 'protmamba/utils.py'),
                                 'protmamba.utils.reorder_masked_sequence': ('utils.html#reorder_masked_sequence', 'protmamba/utils.py'),
                                 'protmamba.utils.save_to_tensorboard': ('utils.html#save_to_tensorboard', 'protmamba/utils.py'),
                                 'protmamba.utils.tokenizer': ('utils.html#tokenizer', 'protmamba/utils.py')}}}
