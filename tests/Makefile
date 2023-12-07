# all: down build up test
# VARIABLES  | $ACCOUNT  | $IP | $API
# AGREGAR ENTER AL FINAL DEL ARCHIVO
.ONESHELL:

set:
	export AWS_PROFILE=$(ACCOUNT); sh getTasks.sh -a; sh setELBS.sh

feedPipelines:
	sh feedPipelines.sh

auroraAcces:
	sh ipAurora.sh -a $(IP)

apiInfo:
	sh apiInfo.sh -a $(API)

verifyAPI:
	sh verifyAPIUsage.sh

capacities:
	sh capacityServices.sh

policy:
	sg getPolicyFromRole.sh -a $(ROLE)

listIPS:
	sh listIPS.sh

envVariables:
	sh variables.sh

black:
	black -l 86 $$(find * -name '*.py')