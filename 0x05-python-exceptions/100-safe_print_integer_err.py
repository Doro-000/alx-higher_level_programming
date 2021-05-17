#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
  try:
    print("{:d}".format(value))
  except ValueError as val_error:
    print("Exception: {}".format(str(val_error)), file=sys.stderr)
    return False
  return True
