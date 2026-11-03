from app.database.neo4j_db import driver, NEO4J_DATABASE


def create_graph_constraints():
    query = """
    CREATE CONSTRAINT ecu_id_unique IF NOT EXISTS
    FOR (ecu:ECU)
    REQUIRE ecu.ecu_id IS UNIQUE
    """

    with driver.session(database=NEO4J_DATABASE) as session:
        session.run(query)


def link_threat_to_ecu(ecu_id: str, attack_type: str):
    query = """
    MERGE (ecu:ECU {ecu_id: $ecu_id})
    MERGE (threat:Threat {attack_type: $attack_type})
    MERGE (threat)-[:AFFECTS]->(ecu)
    RETURN ecu.ecu_id AS ecu_id,
           threat.attack_type AS attack_type
    """

    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(
            query,
            ecu_id=ecu_id,
            attack_type=attack_type
        )
        return result.single().data()


def get_threats_for_ecu(ecu_id: str):
    query = """
    MATCH (threat:Threat)-[:AFFECTS]->(ecu:ECU {ecu_id: $ecu_id})
    RETURN threat.attack_type AS attack_type
    """

    with driver.session(
        database=NEO4J_DATABASE,
        default_access_mode="READ"
    ) as session:
        result = session.run(query, ecu_id=ecu_id)
        return [record["attack_type"] for record in result]


def set_ecu_criticality(ecu_id: str, criticality: int):
    """
    Store the criticality score for an ECU.
    Criticality must be an integer between 0 and 100.
    """

    if not isinstance(criticality, int) or isinstance(criticality, bool):
        raise TypeError("ECU criticality must be an integer")

    if not 0 <= criticality <= 100:
        raise ValueError("ECU criticality must be between 0 and 100")

    query = """
    MERGE (ecu:ECU {ecu_id: $ecu_id})
    SET ecu.criticality = $criticality
    RETURN ecu.ecu_id AS ecu_id,
           ecu.criticality AS criticality
    """

    with driver.session(database=NEO4J_DATABASE) as session:
        result = session.run(
            query,
            ecu_id=ecu_id,
            criticality=criticality
        )
        return result.single().data()


def get_ecu_criticality(ecu_id: str):
    """
    Retrieve the criticality score of an ECU from Neo4j.
    """

    query = """
    MATCH (ecu:ECU {ecu_id: $ecu_id})
    RETURN ecu.ecu_id AS ecu_id,
           ecu.criticality AS criticality
    """

    with driver.session(
        database=NEO4J_DATABASE,
        default_access_mode="READ"
    ) as session:
        result = session.run(query, ecu_id=ecu_id)
        record = result.single()

        if record is None:
            return None

        return record.data()