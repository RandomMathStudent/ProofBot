"""Core exception types for ProofBot."""


class ProofBotError(Exception):
    """Base exception for ProofBot.

    This exception is raised for errors that occur in pipeline assembly,
    backend resolution, and stage orchestration.
    """
