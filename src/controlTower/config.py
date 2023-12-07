import datetime

AWS_CONFIG         = "/Users/r/.aws/config"
AWS_PROFILE_PREFIX = "profile"
ENCODING           = "utf-8"
ERROR              = "error"
FILE_EXTENSION     = "json"
HASH_LGRTHM        = "sha256"
HASH_DIR_LENGTH    = 12
INIT               = "init"
NOW_FILE           = datetime.datetime.now(datetime.timezone.utc).strftime("%m_%d_%Y")
NOW_UTC            = datetime.datetime.now(datetime.timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")
PROCESSING         = "processing"
RECEIPT            = "Makefile"
REGION             = "us-east-1"
ROOTREPOSITORY     = "/Users/r/controlTower"
REGEX_STEPS        = r'(?<=\n)([A-Za-z0-9_]+):(.*?)\n?(\s+(.*?))?\n'
REGEX_IN_FILES     = r'.*?\s([A-z0-9_-]+\.[A-z0-9]+).*?'
SUCCESS            = "success"
TEST_FILE          = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"