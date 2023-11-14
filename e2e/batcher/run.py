from typing import List, Dict
import os
import sys
import uuid
import asyncio
import logging
import logging.config


logging.config.fileConfig(
    'logging.conf',
)

from dynamic_batcher import DynamicBatcher, BatchProcessor

DYNAMIC_BATCHER__BATCH_SIZE = int(os.getenv("DYNAMIC_BATCHER__BATCH_SIZE", "64"))
DYNAMIC_BATCHER__BATCH_TIME = int(os.getenv("DYNAMIC_BATCHER__BATCH_TIME", "2"))


def set_name(bodies: List[Dict]) -> List[Dict]:
    for body in bodies:
        body['name'] = f'{uuid.uuid4()}'

    return bodies


if __name__ == '__main__':
    log = logging.getLogger()
    log.info('test')
    batcher = DynamicBatcher()
    batch_processor = BatchProcessor(
        batch_size=DYNAMIC_BATCHER__BATCH_SIZE,
        batch_time=DYNAMIC_BATCHER__BATCH_TIME,
    )

    asyncio.run(batch_processor.start_daemon(set_name))