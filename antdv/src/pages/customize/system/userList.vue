<script setup lang="ts">
import { h } from 'vue'
import type {MenuProps, PaginationProps} from 'ant-design-vue'
import {Modal} from 'ant-design-vue'
import {ColumnHeightOutlined, PlusOutlined, ReloadOutlined, SettingOutlined, UserOutlined, SearchOutlined, EditOutlined, EllipsisOutlined} from '@ant-design/icons-vue'
import type {UserTableParams, UserTableModel} from '~@/api/customize/system/user'
import {getListApi} from '~@/api/customize/system/user'
import UserFormModal from './userFormModal.vue'

const loginStatusMap = {
  0: '未登录',
  1: '已登录',
}

const switchStatusMap = reactive({
  on: true,
  off: false,
})

const message = useMessage()
const loading = shallowRef(false)
const columns = shallowRef([
  {
    title: '#',
    dataIndex: 'id',
  },
  {
    title: '头像',
    dataIndex: 'avatar',
  },
  {
    title: '所属部门',
    dataIndex: 'department_id',
  },
  {
    title: '直属领导',
    dataIndex: 'parent_id',
  },
  {
    title: '昵称',
    dataIndex: 'nickname',
  },
  {
    title: '用户名',
    dataIndex: 'username',
  },
  {
    title: '电子邮箱',
    dataIndex: 'email',
  },
  {
    title: '最后登录时间',
    dataIndex: 'login_time',
  },
  {
    title: '当前登录状态',
    dataIndex: 'login_status',
  },
  {
    title: '用户状态',
    dataIndex: 'status',
    width: 100,
  },
  {
    title: '',
    dataIndex: 'action',
    width: 100,
  },
])
const formModel = reactive<UserTableParams>({
  nickname: undefined,
  username: undefined,
  email: undefined,
  login_time: undefined,
  login_status: undefined,
  status: undefined,
})
const userFormModal = ref<InstanceType<typeof UserFormModal>>()
const dataSource = shallowRef<UserTableModel[]>([])
const pagination = reactive<PaginationProps>({
  pageSize: 2,
  pageSizeOptions: ['10', '20', '30', '40', '50'],
  current: 1,
  total: 10,
  showSizeChanger: true,
  showQuickJumper: true,
  showTotal: total => `用户总数：${total} 人`,
  onChange(current, pageSize) {
    pagination.pageSize = pageSize
    pagination.current = current
    init()
  },
})
const tableSize = ref<string[]>(['large'])
const sizeItems = ref<MenuProps['items']>([
  {
    key: 'large',
    label: '默认',
    title: '默认',
  },
  {
    key: 'middle',
    label: '中等',
    title: '中等',
  },
  {
    key: 'small',
    label: '紧凑',
    title: '紧凑',
  },
])
const options = computed(() => {
  return columns.value.map((item) => {
    if (item.dataIndex === 'action') {
      return {
        label: item.title,
        value: item.dataIndex,
        disabled: true,
      }
    }
    return {
      label: item.title,
      value: item.dataIndex,
    }
  })
})
const dropdownVisible = ref(false)
const getCheckList = computed(() => columns.value.map(item => item.dataIndex))
const state = reactive({
  indeterminate: false,
  checkAll: true,
  checkList: getCheckList.value,
})

async function init() {
  if (loading.value) return
  loading.value = true
  try {
    const { result } = await getListApi({
      ...formModel,
      current: pagination.current,
      pageSize: pagination.pageSize,
    })
    dataSource.value = result.data
    pagination.current = result.current
    pagination.total = result.totalPage
  }
  catch (e) {
    console.log(e)
  }
  finally {
    loading.value = false
  }
}

async function onSearch() {
  pagination.current = 1
  await init()
}

async function onReset() {
  formModel.nickname = undefined
  formModel.username = undefined
  await init()
}

/**
 * 删除功能
 *  @param record
 *
 */
async function handleDelete(record: UserTableModel) {
  const close = message.loading('删除中......')
  try {
    const res = await deleteApi(record!.id)
    if (res.code === 200)
      await init()
    message.success('删除成功')
  }
  catch (e) {
    console.log(e)
  }
  finally {
    close()
  }
}

/**
 * 新增事件
 *
 */
function handleOk() {
  message.success('操作成功')
  Modal.destroyAll()
  onSearch()
}

function handleAdd() {
  userFormModal.value?.open()
}

function handleEdit(record: UserTableModel) {
  userFormModal.value?.open(record)
}

/**
 * 密度切换
 *
 */
const handleSizeChange: MenuProps['onClick'] = (e) => {
  tableSize.value[0] = e.key as string
}

/**
 * 过滤
 *
 */
function filterAction(value: string[]) {
  return columns.value.filter((item) => {
    if (value.includes(item.dataIndex)) {
      // 为true时，循环遍历的值会暴露出去
      return true
    }
    return false
  })
}

// 备份columns
const filterColumns = ref(filterAction(getCheckList.value))

/**
 * 全选/反选事件
 *
 */
function handleCheckAllChange(e: any) {
  Object.assign(state, {
    checkList: e.target.checked ? getCheckList.value : [],
    indeterminate: true,
  })
  filterColumns.value = e.target.checked ? filterAction(getCheckList.value) : filterColumns.value.filter(item => item.dataIndex === 'action')
}

watch(
    () => state.checkList,
    (val) => {
      state.indeterminate = !!val.length && val.length < getCheckList.value.length
      state.checkAll = val.length === getCheckList.value.length
    },
)

/**
 * 重置事件
 *
 */
function handleResetChange() {
  state.checkList = getCheckList.value
  filterColumns.value = filterAction(getCheckList.value)
}

/**
 * checkbox点击事件
 *
 */
function handleCheckChange(value: any) {
  filterColumns.value = filterAction(value)
}

onMounted(() => {
  init()
})
</script>
<template>
  <div>
    <a-card mb-4>
      <a-form :label-col="{ span: 2 }" :model="formModel">
        <a-row :gutter="[0, 0]">
          <a-col :span="8">
            <a-form-item name="username" label="" class="form-item">
              <a-input v-model:value="formModel.username" placeholder="请输入搜索内容">
                <template #prefix>
                  <search-outlined style="color: rgba(255, 255, 255, 0.45)" />
                </template>
              </a-input>
            </a-form-item>
          </a-col>
          <a-col :span="16">
            <a-space flex justify-end w-full>
              <a-button :loading="loading" type="primary" @click="onSearch">
                查询
              </a-button>
              <a-button :loading="loading" @click="onReset">
                重置
              </a-button>
            </a-space>
          </a-col>
        </a-row>
      </a-form>
    </a-card>
    <a-card>
      <template #title>
        <a-space size="middle">
          <a-button type="primary" @click="handleAdd">
            <template #icon>
              <PlusOutlined />
            </template>
            新增
          </a-button>
        </a-space>
      </template>
      <template #extra>
        <a-space size="middle">
          <a-tooltip title="刷新">
            <ReloadOutlined @click="onSearch" />
          </a-tooltip>
          <a-tooltip title="密度">
            <a-dropdown trigger="click">
              <ColumnHeightOutlined />
              <template #overlay>
                <a-menu v-model:selected-keys="tableSize" :items="sizeItems" @click="handleSizeChange" />
              </template>
            </a-dropdown>
          </a-tooltip>
          <a-tooltip title="列设置">
            <a-dropdown v-model:open="dropdownVisible" trigger="click">
              <SettingOutlined />
              <template #overlay>
                <a-card>
                  <template #title>
                    <a-checkbox v-model:checked="state.checkAll" :indeterminate="state.indeterminate" @change="handleCheckAllChange">
                      列选择
                    </a-checkbox>
                  </template>
                  <template #extra>
                    <a-button type="link" @click="handleResetChange">
                      重置
                    </a-button>
                  </template>
                  <a-checkbox-group v-model:value="state.checkList" :options="options" style="display: flex; flex-direction: column;" @change="handleCheckChange" />
                </a-card>
              </template>
            </a-dropdown>
          </a-tooltip>
        </a-space>
      </template>
      <a-table :loading="loading" :columns="filterColumns" :data-source="dataSource" :pagination="pagination" :size="tableSize[0] as TableProps['size']">
        <template #bodyCell="scope">
          <template v-if="scope?.column?.dataIndex === 'action'">
            <div flex>
              <a-button type="text" :icon="h(EditOutlined)" @click="handleEdit(scope?.record as UserTableModel)" />
              <a-dropdown>
                <a-button type="text" :icon="h(EllipsisOutlined)" />
                <template #overlay>
                  <a-menu>
                    <a-menu-item>
                      <a @click="handleEdit(scope?.record as UserTableModel)">
                        修改密码
                      </a>
                    </a-menu-item>
                    <a-menu-item>
                      <a @click="handleEdit(scope?.record as UserTableModel)">
                        编辑用户
                      </a>
                    </a-menu-item>
                    <a-menu-item>
                      <a-popconfirm
                        title="确定删除该条数据？" ok-text="确定" cancel-text="取消"
                        @confirm="handleDelete(scope?.record as UserTableModel)"
                      >
                        <a>
                          删除用户
                        </a>
                      </a-popconfirm>
                    </a-menu-item>
                  </a-menu>
                </template>
              </a-dropdown>
            </div>
          </template>
          <template v-if="scope?.column?.dataIndex === 'avatar'">
            <a-avatar>
              <template #icon><UserOutlined /></template>
            </a-avatar>
          </template>
          <template v-if="scope?.column?.dataIndex === 'login_status'">
            <a-tag v-if="scope?.record?.login_status === 1" color="green">
              {{ loginStatusMap[scope?.record?.login_status as keyof typeof loginStatusMap] as string }}
            </a-tag>
            <a-tag v-else color="orange">
              {{ loginStatusMap[scope?.record?.login_status as keyof typeof loginStatusMap] as string }}
            </a-tag>
          </template>
          <template v-if="scope?.column?.dataIndex === 'status'">
            <a-switch v-if="scope?.record?.status" v-model:checked="switchStatusMap['on']" disabled />
            <a-switch v-else v-model:checked="switchStatusMap['off']" size="small" disabled />
          </template>
        </template>
      </a-table>
    </a-card>
    <user-form-modal ref="userFormModal" @ok="handleOk" />
  </div>
</template>
<style lang="less" scoped>
.form-item {
  margin-bottom: 0;
}
</style>
