from neuralcompress.procedures.train import train
from neuralcompress.models.bcae_trainer import BCAETrainer


data_path   = '/home/qircai/NeuralCompression/outer'
data_config = {
    'batch_size' : 32,
    'train_sz'   : 960,
    'valid_sz'   : 320,
    'test_sz'    : 320,
    'is_random'  : True,
}
epochs      = 2000
valid_freq  = 5
save_path   = '/home/qircai/NeuralCompression/checkpoints/'
save_freq   = 20

train(
    data_path   = data_path,
    data_config = data_config,
    trainer     = BCAETrainer(),
    epochs      = epochs,
    valid_freq  = valid_freq,
    save_path   = save_path,
    save_freq   = save_freq
)
