# Import wandb
import wandb

# Initialize a new run
run = wandb.init(project='demo1')

# Log a parameter
run.log({'accuracy': 0.9})

# Finish the run
run.finish()