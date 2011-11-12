#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os

def evaluate(step_size):
	step_size = str(step_size)
	arg = "./predict.py " + step_size
	os.system(arg)

parser = argparse.ArgumentParser(description="Iterate over threshold values")
parser.add_argument("step_size", help="How much shall the threshold be incremented for every iteration (threshold can vary from 0.0 - 1.0)")
args = parser.parse_args()
evaluate(args.step_size)
