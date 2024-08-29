import { basicRouteMap } from './router-modules'

export default [
  {
    path: '/system',
    redirect: '/system/users',
    name: 'System',
    meta: {
      title: '系统管理',
      icon: 'DashboardOutlined',
    },
    component: basicRouteMap.RouteView,
    children: [
      {
        path: '/system/users',
        name: 'SystemUsers',
        component: () => import('~/pages/customize/system/userList.vue'),
        meta: {
          title: '账号管理',
        },
      },
      {
        path: '/system/roles',
        name: 'SystemRole',
        component: () => import('~/pages/customize/system/roleList.vue'),
        meta: {
          title: '角色管理',
        },
      },
      {
        path: '/system/permissions',
        name: 'SystemPermissions',
        component: () => import('~/pages/customize/system/permissionList.vue'),
        meta: {
          title: '权限管理',
        },
      },
      {
        path: '/system/departments',
        name: 'SystemDepartments',
        component: () => import('~/pages/customize/system/departmentList.vue'),
        meta: {
          title: '部门管理',
        },
      },
    ]
  }
]
