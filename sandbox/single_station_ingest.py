import boto3
from botocore import UNSIGNED
from botocore.config import Config


def main():
  
    endpoint= 'https://www.ncei.noaa.gov/oa'
    bucket = 'global-historical-climatology-network'
    prefix = 'daily/access/by-station/'

    client = boto3.client("s3",endpoint_url=endpoint, config=Config(signature_version=UNSIGNED))
    response = client.list_objects(Bucket=bucket,Delimiter='/',Prefix=prefix)

    stations_and_path = []
    station_list = {}
    all_stations =  response['Contents']
    for station in all_stations:
        stations_and_path.append(station['Key'][-19:-8])
        station_list[station['Key'][-19:-8]] = station['Key']

    print(f"All Stations: {all_stations}")

if __name__ == "__main__":
    main()