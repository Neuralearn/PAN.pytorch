# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 22:00
# @Author  : zhoujun

from __future__ import print_function
import os
from utils import load_json

config = load_json('config.json')
os.environ['CUDA_VISIBLE_DEVICES'] = ','.join([str(i) for i in config['trainer']['gpus']])

from models import get_model, get_loss
from data_loader import get_dataloader
from trainer import Trainer
import torch

def main(config):
    train_loader = get_dataloader(config['data_loader']['type'], config['data_loader']['args'])


    #checkpoint = torch.load('output/PANNet_latest.pth')

    #config = checkpoint['config']
        
    #config['arch']['args']['pretrained'] = True

    model = get_model(config)
    
    #model.load_state_dict(checkpoint['state_dict'])
    
    criterion = get_loss(config).cuda()

    trainer = Trainer(config=config,
                      model=model,
                      criterion=criterion,
                      train_loader=train_loader)
    trainer.train()


if __name__ == '__main__':
    main(config)
