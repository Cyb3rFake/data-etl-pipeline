"""Main ETL pipeline for data processing and transformation."""
import os
import pandas as pd
from sqlalchemy import create_engine
from loguru import logger
from dotenv import load_dotenv

load_dotenv()

class ETLPipeline:
    """Extract, Transform, Load pipeline."""
    
    def __init__(self, db_url=None):
        """Initialize ETL pipeline.
        
        Args:
            db_url: Database connection string
        """
        self.db_url = db_url or os.getenv('DATABASE_URL')
        self.engine = None
        logger.info("ETL Pipeline initialized")
    
    def connect(self):
        """Establish database connection."""
        try:
            self.engine = create_engine(self.db_url)
            logger.info("Connected to database")
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise
    
    def extract(self, source_path):
        """Extract data from CSV source.
        
        Args:
            source_path: Path to CSV file
        
        Returns:
            DataFrame with extracted data
        """
        logger.info(f"Extracting data from {source_path}")
        df = pd.read_csv(source_path)
        logger.info(f"Extracted {len(df)} records")
        return df
    
    def transform(self, df):
        """Transform data.
        
        Args:
            df: Input DataFrame
        
        Returns:
            Transformed DataFrame
        """
        logger.info("Transforming data")
        # Remove duplicates
        df = df.drop_duplicates()
        # Handle missing values
        df = df.fillna(0)
        logger.info(f"Transformed {len(df)} records")
        return df
    
    def load(self, df, table_name):
        """Load data to database.
        
        Args:
            df: DataFrame to load
            table_name: Target table name
        """
        if not self.engine:
            self.connect()
        
        logger.info(f"Loading {len(df)} records to {table_name}")
        df.to_sql(table_name, self.engine, if_exists='append', index=False)
        logger.info(f"Successfully loaded data to {table_name}")
    
    def run(self, source_path, table_name):
        """Run complete ETL pipeline.
        
        Args:
            source_path: Source data file
            table_name: Target database table
        """
        try:
            df = self.extract(source_path)
            df = self.transform(df)
            self.load(df, table_name)
            logger.info("ETL pipeline completed successfully")
        except Exception as e:
            logger.error(f"ETL pipeline failed: {e}")
            raise

if __name__ == '__main__':
    pipeline = ETLPipeline()
    # Example: pipeline.run('data/input.csv', 'output_table')
    logger.info("ETL Pipeline ready")
