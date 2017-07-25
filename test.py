from bravado.client import SwaggerClient
from bravado.swagger_model import load_file

if __name__ == '__main__':

    config = {
        'also_return_response': True,
        'validate_responses': True,
        'validate_requests': True,
        'validate_swagger_spec': True,
        'use_models': True
    }

    client = SwaggerClient.from_spec(load_file('swagger.yaml'), config=config)

    CreateDBInstanceRequest = client.get_model('CreateDBInstanceRequest')

    create_db_request = CreateDBInstanceRequest(instanceId='xx'
                                                , instanceClass='db.t1.micro'
                                                , engine='MySQL'
                                                , port=9999
                                                , availableZone='AZX-aaaa'
                                                , chaos_fields_foo = 'xxxxxxx999')

    rds_instance, http = client.instance.createInstance(body=create_db_request).result()

    print rds_instance
    print rds_instance['instance']['engine']