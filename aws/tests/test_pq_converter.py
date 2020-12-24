import pytest
import os


@pytest.mark.usefixtures("read_event")
class TestReadS3Event:
    def test_bucket(self, read_event):
        assert read_event[0] == "test-bucket"

    def test_key(self, read_event):
        assert read_event[1] == "test-key"


@pytest.mark.usefixtures("read_csv")
class TestMakeDataframe:
    def test_df_row_length(self, read_csv):
        assert len(read_csv) == 980

    def test_df_col_length(self, read_csv):
        assert len(read_csv.columns) == 9


@pytest.mark.usefixtures("create_pq")
class TestCreateParquet:
    def test_is_exist_parquet(self, create_pq):
        assert os.path.exists(create_pq) == True
