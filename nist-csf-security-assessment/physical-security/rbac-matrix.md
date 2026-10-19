# Physical access role matrix (least privilege)

Y = access granted, N = denied, – = not applicable. Screenshot: `rbac-matrix.png`.

| Role | Lobby | Assigned workspace | Office | Database room | Server room | IT admin office | Visitor area |
|---|---|---|---|---|---|---|---|
| Employee | Y | – | Y | N | N | N | N |
| Team lead / manager | Y | – | Y | N | N | N | N |
| IT staff / technician | Y | – | Y | Y | Y | Y | N |
| Security staff | Y | – | Y | Y | Y | N | N |
| Contractor / vendor | Y | Y | N | N | N | N | N |
| Visitor / guest | Y | – | N | N | N | N | Y |
| Executive / C-level | Y | – | Y | Y | Y | Y | N |

Design notes:
- Regular employees get office access during business hours only (time-of-day restriction on the badge system).
- Only IT, security and executive roles reach the database and server rooms.
- Contractors get an assigned workspace at the administrator's discretion and nothing else.
- Roles can be added or changed without redesigning the matrix.
