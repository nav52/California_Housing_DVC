# California Housing Prediction

This project utilizes the dataset on california housing to predict on the median house value of the data.
It'll be a structured and clean end-to-end implementation.

## Dataset
https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz



## commands - 

### create a new env
```bash
bash init_setup.sh
```

### activate new env
```bash
conda activate ./env
```

### init DVC
```bash
dvc init
```
## workflow - 
1. update config.yaml
2. update params.yaml
3. update secrets.yaml
4. update entity
5. update Config manager
6. update component
7. update pipeline
8. test run everything
9. update dvc.yaml and run all stage