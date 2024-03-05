import connector_dynamo
import connector_oracle

conn = connector_oracle.connOracle()
#connector_dynamo.connDynamo()


table = connector_dynamo.connDynamo()
connector_dynamo.read_item_table(table,"PM_Review_M");


if conn:
    pass
    