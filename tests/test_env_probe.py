import os


def test_fork_pr_must_not_receive_org_secrets():
    # Boolean signal only. The value is never printed, logged or transmitted.
    assert os.environ.get("MERGIFY_TOKEN", "") == "", "SECRET-PRESENT-IN-FORK-PR"
