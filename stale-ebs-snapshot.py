import boto3
import datetime

def lambda_handler(event, context):
    #Initialize the AWS client ec2
    ec2 = boto3.client('ec2')

    #define the retention period for snapshots in days
    retention_days = 30
    
    #calculate the retention date
    retention_date = datetime.datetime.now() - datetime.timedelta(days=retention_days)

    # List all EBS snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self']) ['Snapshots']

    #Identify and log stale snapshots
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        start_time = snapshot['StartTime']
        #check if the snapshot is older than the retention period
        if start_time < retention_date:
            print(f"Stale snapshot {snapshot_id} created on {start_time}")

             # Delete the stale snapshot(uncomment below lisnes of code to delete the snapshots)

            #ec2.delete_snapshot(SnapshotId=snapshot_id)
            #print(f"Deleted stale snapshot {snapshot_id}")