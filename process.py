from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("terminus_delivery").getOrCreate()

if __name__ == "__main__":
    # Parse data from CSV files into data frames
    df_stations = spark.read.option("header", "true").csv("/tmp/stations.csv.gz")
    df_trips = spark.read.option("header", "true").csv("/tmp/trips.csv.gz")

    # Log bad/corrupted records
    # TODO Need to somehow list records that are corrupted or have bad data
    # TODO Need to also add code after the join that logs records with a bad or missing start/end station id

    # Join trips to stations to pull in station name. Format data according to delivery schema\
    df_results = df_trips.join(
        df_stations, df_trips.start_station_id == df_stations.id
    ).selectExpr(
        "trip_duration",
        "start_time",
        "stop_time",
        "start_station_id",
        "name as start_station_name",
        "end_station_id",
        "birth_year",
        "gender",
    )
    df_results.show()
    df_results = df_results.join(
        df_stations, df_results.end_station_id == df_stations.id
    ).selectExpr(
        "trip_duration",
        "start_time",
        "stop_time",
        "start_station_id",
        "start_station_name",
        "end_station_id",
        "name as end_station_name",
        "birth_year",
        "gender",
    )
    df_results.show()
    # Save results to a local file ready to be uploaded
    df_results.coalesce(1).write.option("header", "true").csv(
        "/tmp/results/", mode="overwrite"
    )
