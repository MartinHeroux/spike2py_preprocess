from pathlib import Path

import pytest

from spike2py_preprocess.subject import SubjectPaths
from spike2py.trial import TrialInfo, Trial

STUDY1 = Path(__file__).parent / "data" / "study1"
SECTIONED_FILE = (
    Path(__file__).parent / "data" / "study3" / "sub01" / "raw" / "01_DATA_000_C_B.mat"
)


@pytest.fixture()
def study1_path():
    return STUDY1


@pytest.fixture()
def study_details_json():
    return STUDY1 / "study_info.json"


@pytest.fixture()
def study_details_dict():
    return {
        "channels": ["FDI", "W_EXT", "stim"],
        "name": "TSS_H-reflex",
        "subjects": ["sub01", "sub02"],
    }


@pytest.fixture()
def sub01_paths():
    paths = SubjectPaths(home=STUDY1 / "sub01")
    paths.create()
    return paths


@pytest.fixture()
def sub02_paths():
    paths = SubjectPaths(home=STUDY1 / "sub02")
    paths.create()
    return paths


@pytest.fixture()
def temp_path(tmp_path):
    return tmp_path


@pytest.fixture()
def sub1_trial_info(sub01_paths, temp_path):
    trial_info = TrialInfo(
        file=sub01_paths.raw / "sub01_DATA000_H_B.mat",
        channels=None,
        name="kHz_biphasic",
        subject_id="sub01",
        path_save_trial=temp_path,
        path_save_figures=temp_path,
    )
    return trial_info


@pytest.fixture()
def sub1_data(sub1_trial_info):
    data = Trial(sub1_trial_info)
    return data


@pytest.fixture()
def sub2_trial_info(sub02_paths, temp_path):
    trial_info = TrialInfo(
        file=sub02_paths.raw / "sub02_DATA000_H_B.mat",
        channels=None,
        name="kHz_biphasic",
        subject_id="sub02",
        path_save_trial=temp_path,
        path_save_figures=temp_path,
    )
    return trial_info


@pytest.fixture()
def channels_file1():
    return [
        ("Ta", "waveform"),
        ("Sol", "waveform"),
        ("Abp", "waveform"),
        ("Ds8", "event"),
        ("Mmax", "event"),
        ("Pain", "waveform"),
        ("W_Ext", "waveform"),
        ("Fdi", "waveform"),
        ("Stim", "waveform"),
        ("Keyboard", "keyboard"),
        ("Stimcode", "keyboard"),
    ]


@pytest.fixture()
def subject_preprocess_details():
    return {"Fdi": {"remove_mean": "", "lowpass": "cutoff=100"}}


@pytest.fixture()
def study_preprocess_details():
    return {
        "Fdi": {"remove_mean": "", "lowpass": {"cutoff": 200}},
        "Ecr": {"remove_mean": "", "bandstop": {"cutoff": [49, 51]}},
        "Stim": {"lowpass": {"cutoff": 20, "order": 8}},
    }


@pytest.fixture()
def study_preprocess_details_wrong():
    return {
        "marty": {"remove_mean": "", "lowpass": {"cutoff": 200}},
        "ecr": {"remove_mean": "", "bandstop": {"cutoff": [49, 51]}},
        "stim_intensity": {"lowpass": {"cutoff": 20, "order": 8}},
    }


@pytest.fixture()
def attribute_error_message():
    return (
        "Following spike2py data does not have requested attribute: \n"
        "\tdata.marty.remove_mean()\n"
        "kHz_biphasic\n"
    )


@pytest.fixture()
def data_with_sections():
    trial_info = TrialInfo(
        file=Path(SECTIONED_FILE),
        name="conventional_biphasic",
        subject_id="sub01",
        path_save_figures=Path(SECTIONED_FILE).parent.parent / "figures",
        path_save_trial=Path(SECTIONED_FILE).parent.parent / "proc",
    )
    return Trial(trial_info)


@pytest.fixture()
def not_path_error_message():
    return (
        "\t\tAll paths must be pathlib.Path objects, not strings.\n"
        "\t\tPlease correct for: \n"
    )


@pytest.fixture()
def uneven_textmarks_error_message():
    return (
        "01_DATA_000_C_B.mat has an uneven number of TextMarks on the Memory channel. "
        "Please correct and rerun.\n"
    )


@pytest.fixture()
def non_matching_section_names_error_message():
    return (
        "\t\t01_DATA_000_C_B.mat has pairs of TextMarks on the Memory channel that do "
        "not match.\n"
        "\t\t\tPlease correct and rerun.\n"
    )


@pytest.fixture()
def section_file_path():
    return Path(SECTIONED_FILE)
