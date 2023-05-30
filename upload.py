import pysftp
import glob


if __name__ == '__main__':
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    # Check results folder for file and rename to human readable name
    filename = glob.glob("/tmp/results/part-*.csv")[0]
    # Connect to SFTP and upload results file from tmp
    with pysftp.Connection("34.74.110.44", username="etl_engineer", password="meSt8Y6DJ6u3ENX4", cnopts=cnopts) as sftp:
        sftp.put(filename, "/upload/john_walz_trips.csv")
