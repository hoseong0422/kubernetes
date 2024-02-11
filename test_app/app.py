from random import choice
from json_logger_stdout import JSONLoggerStdout
import time

TOPICS = [
    'test_topic_A',
    'test_topic_B',
    'test_topic_C',
    ]


while True:
    TOPIC = choice(TOPICS)
        
    logger = JSONLoggerStdout(
        topic=TOPIC,
    )
    logger.info("Test Logger Message")
    
    time.sleep(5)