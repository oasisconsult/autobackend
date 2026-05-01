from app.models.tenant import Tenant


class TenantProvisioning:

    def provision(self, db, tenant_id: str):

        tenant = Tenant(id=tenant_id, name=f"Tenant-{tenant_id}")

        db.add(tenant)
        db.commit()

        return tenant