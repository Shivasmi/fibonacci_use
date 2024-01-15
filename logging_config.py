import logging

logging.basicConfig(filename='logging.py', # Specify the filename 
                    level=logging.DEBUG, # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) 
                    format='%(asctime)s - %(levelname)s - %(message)s')
def setup_logging(): 
    logging.debug('This is a debug message') 
    logging.info('This is an info message') 
    logging.warning('This is a warning message') 
    logging.error('This is an error message') 
    logging.critical('This is a critical message')

if __name__ == "__main__": # Call the example function 
    
    setup_logging()
