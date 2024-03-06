import connector_dynamo
import connector_oracle

# Establish connection to Oracle database
conn = connector_oracle.connOracle()

# Establish connection to DynamoDB table
table = connector_dynamo.connDynamo()

# Read data from DynamoDB table
data = connector_dynamo.read_item_table(table, "PM_Review_M")


# Check if the Oracle connection is established
if conn:
    for index, d in enumerate(data):

        timeID = d["Date"]
        customerID = int(d["customerID"])
        score = int(d["score"])
        
        # Construct INSERT INTO statement
        query = "INSERT INTO DW_FT_RATING(timeID, customerID, Score) VALUES (TO_DATE(:1, 'YYYY-MM-DD'), :2, :3)"
        # Data to be inserted into Oracle table
        data_Oracle = (timeID, customerID, score)
        
        # Execute the query
        connector_oracle.insert_data(conn, query, data_Oracle)
    
    


