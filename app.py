import logging

# Configure logging
logging.basicConfig(
    filename='/mnt/u/my_projects/discovery_log.txt',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def main():
    logging.info("Starting UnifiedTechPlatform application...")

if __name__ == "__main__":
    main()
