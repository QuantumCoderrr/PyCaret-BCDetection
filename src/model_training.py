# Auto-generated from notebook

# train and test the models
compare_models()

# select the best model
model = create_model('catboost')

# hyperparameter tuning
best_model = tune_model(model)

