import os

MODELS_DIR_PATH = "/mnt/Storage1/models"
RESOURCES_DIR_PATH = "/mnt/Storage1/resources"
COPY_RESOURCES = False


def check_dir_or_mkdir(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        return

    os.mkdir(path=dir_path)


def is_not_symlink():
    return not os.path.exists(current_dir) or not os.path.isdir(current_dir)


if "__main__" == __name__:
    script_dir_path = os.path.dirname(__file__)

    database_dir = "database"
    documents_database_dir = "documents"
    questions_database_dir = "questions"
    vector_store_database_dir = "vector_store"
    results_database_dir = "results"

    current_dir = os.path.join(script_dir_path, database_dir)
    check_dir_or_mkdir(current_dir)

    current_dir = os.path.join(script_dir_path, database_dir, results_database_dir)
    check_dir_or_mkdir(current_dir)

    current_dir = os.path.join(script_dir_path, database_dir, documents_database_dir)
    if COPY_RESOURCES:
        if is_not_symlink():
            os.symlink(
                src=RESOURCES_DIR_PATH + "/" + documents_database_dir,
                dst=current_dir,
                target_is_directory=True,
            )
    else:
        check_dir_or_mkdir(current_dir)

    current_dir = os.path.join(script_dir_path, database_dir, questions_database_dir)
    if COPY_RESOURCES:
        if is_not_symlink():
            os.symlink(
                src=RESOURCES_DIR_PATH + "/" + questions_database_dir,
                dst=current_dir,
                target_is_directory=True,
            )
    else:
        check_dir_or_mkdir(current_dir)

    current_dir = os.path.join(script_dir_path, database_dir, vector_store_database_dir)
    if COPY_RESOURCES:
        if is_not_symlink():
            os.symlink(
                src=RESOURCES_DIR_PATH + "/" + vector_store_database_dir,
                dst=current_dir,
                target_is_directory=True,
            )
    else:
        check_dir_or_mkdir(current_dir)

    models_dir = "models"
    current_dir = os.path.join(script_dir_path, models_dir)
    if is_not_symlink():
        os.symlink(
            src=MODELS_DIR_PATH,
            dst=current_dir,
            target_is_directory=True,
        )
