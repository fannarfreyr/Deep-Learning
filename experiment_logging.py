import os
from datetime import datetime
import traceback

class ExperimentLogger:
    def __init__(self, log_file="experiment_log.md", active=True, show_console=False):
        """
        Parameters:
        - log_file (str): path to the markdown log file.
        - active (bool): if False, disables all logging.
        - show_console (bool): if True, prints full log entry to console.
        """
        self.active = True 
        """Turn it to 'False' if you want to disable the logging"""
        self.show_console = show_console
        self.log_file = log_file

        self.reset()

        if self.active and not os.path.exists(self.log_file):
            with open(self.log_file, "w", encoding="utf-8") as f:
                f.write("# Experiment Log\n\n")

    def reset(self):
        """Reset all experiment fields."""
        self.name = False
        self.changes = False
        self.reason = False
        self.results = False
        self.errors = False
        self.notes = False
        self.metrics = False

    def set(self, **kwargs):
        """Update experiment fields."""
        if not self.active:
            return
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"⚠️ Unknown field: {key}")

    def record_metrics(self, epoch, acc, loss):
        """Add metrics progressively."""
        if not self.active:
            return
        if self.metrics is False:
            self.metrics = {}
        self.metrics[epoch] = {"acc": acc, "loss": loss}

    def commit(self):
        """Write the log to Markdown file."""
        if not self.active:
            print("🟡 Logging is disabled. Skipping log.")
            return

        if not self.name:
            print("⚠️ Experiment name not set. Skipping log.")
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"## Experiment: {self.name}\n"
        entry += f"**Date:** {timestamp}\n\n"

        if self.changes: entry += f"**Changes Made:**\n{self.changes}\n\n"
        if self.reason: entry += f"**Reason for Change:**\n{self.reason}\n\n"
        if self.metrics:
            entry += "**Training Metrics:**\n"
            for epoch, metric in self.metrics.items():
                entry += f"- Epoch {epoch}: Accuracy={metric['acc']:.4f}, Loss={metric['loss']:.4f}\n"
            entry += "\n"
        if self.results: entry += f"**Final Results:**\n{self.results}\n\n"
        if self.errors: entry += f"**Errors / Issues:**\n{self.errors}\n\n"
        if self.notes: entry += f"**Notes / Insights:**\n{self.notes}\n\n"
        entry += "---\n\n"

        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)

        if self.show_console:
            print("\n Experiment Log Preview:\n")
            print(entry)

        print(f"✅ Experiment '{self.name}' logged successfully.")
        self.reset()

    def capture_errors(self, func, *args, **kwargs):
        """Run a function and capture any errors automatically."""
        if not self.active:
            return func(*args, **kwargs)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self.errors = f"{e}\n\nTraceback:\n{traceback.format_exc()}"
            return None
