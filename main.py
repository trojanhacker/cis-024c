import helper;
import argparse;

parser = argparse.ArgumentParser(description='Calculate the sum of two numbers');
parser.add_argument('num1', type=int, help='First number');
parser.add_argument('num2', type=int, help='Second number');
args = parser.parse_args();

if __name__ == '__main__':
    print (helper.sum(args.num1, args.num2));