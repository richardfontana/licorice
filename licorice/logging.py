
import logging

main_logger = logging.getLogger('licorice')
main_logger.addHandler(logging.StreamHandler())
main_logger.setLevel(logging.INFO)

logger = main_logger

def set_debug():
    main_logger.setLevel(logging.DEBUG)
