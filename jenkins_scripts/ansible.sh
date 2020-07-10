#!/bin/bash

cd .. << EOF

ansible-playbook -v -i inventory playbook.yaml

EOF
