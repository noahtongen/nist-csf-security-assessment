-- Verify Transparent Data Encryption (TDE) status on SQL Server.
-- Output screenshot: tde-verification-output.png

-- 1) Which databases have TDE enabled?
SELECT
    name AS DatabaseName,
    is_encrypted AS IsTDEEnabled,
    create_date,
    recovery_model_desc
FROM sys.databases
ORDER BY name;

-- 2) Encryption state, algorithm and key length per database.
--    encryption_state = 3 means "encrypted".
SELECT
    db_name(database_id) AS DatabaseName,
    encryption_state,
    key_algorithm,
    key_length
FROM sys.dm_database_encryption_keys;
