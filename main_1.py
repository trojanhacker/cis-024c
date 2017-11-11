import sorthelper;
import argparse;

parser = argparse.ArgumentParser(description='Sort of a list of numbers');
parser.add_argument('List', nargs='+', default=[], help='A List');
args = parser.parse_args();

if __name__ == '__main__':
    print (sorthelper.sortNumbers(args.List));