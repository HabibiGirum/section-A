# Example 1

set1 = {10, 20, 30}
set2 = {40, 50, 60}
disjoint_result = set1.isdisjoint(set2)

print(disjoint_result)

# Example 2

admin_permissions = {'edit', 'delete', 'create'}
viewer_permissions = {'view'}
permissions_disjoint = admin_permissions.isdisjoint(viewer_permissions)

print(permissions_disjoint)