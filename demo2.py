import wandb
import time
import random

# Initialize a new run with a custom name
run = wandb.init(project='demo2', name='advanced_demo')

# Define hyperparameters
config = run.config
config.learning_rate = 0.001
config.batch_size = 32
config.epochs = 10

# Simulate training process
for epoch in range(config.epochs):
    # Simulate training loss and accuracy
    loss = 1.0 / (epoch + 1) + random.uniform(0, 0.1)
    accuracy = 0.5 + random.uniform(0, 0.4)

    # Log metrics
    run.log({'epoch': epoch + 1, 'loss': loss, 'accuracy': accuracy})

    # Simulate a delay
    time.sleep(0.5)

# Finish the run
run.finish()