import pysftp


if __name__ == "__main__":
    # input file names on SFTP server
    files = ["stations.csv.gz", "trips.csv.gz"]

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    # Connect to SFTP and download trips and stations to tmp
    with pysftp.Connection(
        "34.74.110.44",
        username="etl_engineer",
        password="meSt8Y6DJ6u3ENX4",
        cnopts=cnopts,
    ) as sftp:
        for file in files:
            sftp.get(file, "/tmp/" + file)
