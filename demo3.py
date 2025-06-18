import wandb
import time
import random
from datetime import datetime

# Initialize a new run with a custom name
run = wandb.init(project='demo3', name='data_logging_demo')

# Define hyperparameters
config = run.config
config.learning_rate = 0.001
config.batch_size = 32
config.epochs = 10

# Log additional metadata
run.log({'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

# Simulate training process
for epoch in range(config.epochs):
    # Simulate training loss and accuracy
    loss = 1.0 / (epoch + 1) + random.uniform(0, 0.1)
    accuracy = 0.5 + random.uniform(0, 0.4)

    # Log metrics
    run.log({'epoch': epoch + 1, 'loss': loss, 'accuracy': accuracy})

    # Simulate a delay
    time.sleep(0.5)

# Log a sample dataset
run.log({'sample_data': [random.random() for _ in range(10)]})

# Finish the run
run.finish()