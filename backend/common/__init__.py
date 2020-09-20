class JobStatus:
    PENDING, SUCCESS, FAILED, DELETED = (
        "pending",
        "success",
        "failed",
        "deleted",
    )

    CHOICES = [
        (PENDING, "Pending"),
        (SUCCESS, "Success"),
        (FAILED, "Failed"),
        (DELETED, "Deleted"),
    ]
