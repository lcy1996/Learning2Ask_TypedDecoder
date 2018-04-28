# Learning2Ask_TypedDecoder
---
The code for the paper "Learning to Ask Questions in Open-domain Conversational Systems with Typed Decoders" on ACL2018

Cite this paper:
```
@inproceedings{wang2018learning,
  title={Learning to Ask Questions in Open-domain Conversational Systems with Typed Decoders},
  author={Wang, Yansen and Liu, Chenyi and Huang, Minlie and Nie, Liqiang},
  booktitle={ACL},
  year={2018}
}
```

## Usage:
### STD:

### HTD:
Command ```python main.py {--[option1]=[value1] --[option2]=[value2] ... }```

Options(=[default_value]):
* ```--is_train=True``` Set to True for training and False from inference.
* ```--symbols=20000``` Size of vocabulary.
* ```--embed_units=100``` Size of word embedding.
* ```--units=512``` Size of each model layer.
* ```--layers=4``` Number of layers in the model.
* ```--batch_size=50``` Batch size to use during training. **Please set to 1 during inference or the PMI mechanism can't work properly.**
* ```--data_dir=./data``` Data directory.
* ```--train_dir=./train``` Training directory.
* ```--per_checkpoint=1000``` How many steps to do per checkpoint.
* ```--check_version=0``` The version for continuing training or for inferencing.
* ```--log_parameters=True``` Set to True to show the parameters.
* ```--inference_path=""``` Set filename of inference, empty for screen input.
* ```--PMI_path=./PMI``` PMI director.
* ```--keywords_per_sentence=12``` How many keywords will be included.
* ```--question_data=True``` **(Deprecated, please set to True)** An unused option in the final version.

The file ```train.sh``` and ```infer.sh``` contain example commands for training and inference. You can use them with the ```sh``` command.