<script setup lang="ts">
import { h } from 'vue'
import type { UnwrapRef } from 'vue'
import { cloneDeep } from 'lodash-es'
import type { MenuProps, PaginationProps, TableProps } from 'ant-design-vue'
import { Modal } from 'ant-design-vue'
import {
  ColumnHeightOutlined,
  PlusOutlined,
  ReloadOutlined,
  SettingOutlined,
  SearchOutlined,
  CheckOutlined,
  EditOutlined,
  EllipsisOutlined
} from '@ant-design/icons-vue'
import {
  DepartmentTableParams,
  DepartmentTableModel,
  getListApi
} from '@/api/customize/system/department'
import UserFormModal from './component/userFormModal.vue'

const statusMap = {
  0: '异常',
  1: '正常',
}

const message = useMessage()
const loading = shallowRef(false)
const columns = shallowRef([
  {
    title: '编号',
    dataIndex: 'id',
  },
  {
    title: '上级部门',
    dataIndex: 'parents',
  },
  {
    title: '部门名称',
    dataIndex: 'name',
  },
  {
    title: '创建时间',
    dataIndex: 'created_time',
  },
  {
    title: '创建人',
    dataIndex: 'created_by',
  },
  {
    title: '更新时间',
    dataIndex: 'updated_time',
  },
  {
    title: '更新人',
    dataIndex: 'updated_by',
  },
  {
    title: '状态',
    dataIndex: 'status',
    width: 100,
  },
  {
    title: '操作',
    dataIndex: 'action',
    width: 100,
  },
])
const formModel = reactive<DepartmentTableParams>({
  name: '',
})
const departmentFormModal = ref<InstanceType<typeof UserFormModal>>()
const dataSource = shallowRef<DepartmentTableModel[]>([])
const pagination = reactive<PaginationProps>({
  pageSize: 2,
  pageSizeOptions: ['10', '20', '30', '40', '50'],
  current: 1,
  total: 10,
  showSizeChanger: true,
  showQuickJumper: true,
  showTotal: total => `部门总数：${total} `,
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
    const { data } = await getListApi({
      ...formModel,
      current: pagination.current,
      pageSize: pagination.pageSize,
    })
    dataSource.value = data.list
    pagination.current = data.current
    pagination.total = data.totalPage
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
  formModel.name = ''
  await init()
}

/**
 * 新增事件
 *
 */
function handleSubmit() {
  message.success('操作成功')
  Modal.destroyAll()
  onSearch()
}

function handleAdd() {
  departmentFormModal.value?.open()
}

function handleEdit(record: DepartmentTableModel) {
  departmentFormModal.value?.open(record)
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

/**
 * 编辑单元格
 *
 */
const editableData: UnwrapRef<Record<string, DepartmentTableModel>> = reactive({})
const editableCellEdit = (id: string) => {
  editableData[id] = cloneDeep(dataSource.value.filter(item => id === item.id)[0])
}
const editableCellSave = (id: string) => {
  Object.assign(dataSource.value.filter(item => id === item.id)[0], editableData[id])
  delete editableData[id]
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
            <a-form-item name="name" label="" class="form-item">
              <a-input v-model:value="formModel.name" placeholder="请输入搜索内容">
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
        <template #bodyCell="{ column, text, record }">
          <template v-if="column.dataIndex === 'action'">
            <div flex>
              <a-button type="text" :icon="h(EditOutlined)" @click="handleEdit(record as DepartmentTableModel)" />
              <a-dropdown>
                <a-button type="text" :icon="h(EllipsisOutlined)" />
                <template #overlay>
                  <a-menu>
                    <a-menu-item>
                      <a @click="handleEdit(record as DepartmentTableModel)">
                        编辑
                      </a>
                    </a-menu-item>
                    <a-menu-item>
                      <a-popconfirm
                          title="确定删除该条数据？" ok-text="确定" cancel-text="取消"
                          @confirm="handleDelete(record as DepartmentTableModel)"
                      >
                        <a>
                          删除
                        </a>
                      </a-popconfirm>
                    </a-menu-item>
                  </a-menu>
                </template>
              </a-dropdown>
            </div>
          </template>
          <template v-if="column.dataIndex === 'parents'">
            <a-tag color="green">
              <span v-for="(item, index) in record.parents" :key="index">
                <span>{{ item.name }}</span>
                <span v-if="index < record.parents.length - 1"> - </span>
              </span>
            </a-tag>
          </template>
          <template v-if="column.dataIndex === 'name'">
            <div class="editable-cell">
              <div v-if="editableData[record.id]">
                <a-input v-model:value="editableData[record.id].name" class="editable-cell-input" @pressEnter="editableCellSave(record.id)" />
                <check-outlined class="editable-cell-icon-check" @click="editableCellSave(record.id)" />
              </div>
              <div v-else>
                {{ text || '' }}
                <edit-outlined class="editable-cell-icon" @click="editableCellEdit(record.id)" />
              </div>
            </div>
          </template>
          <template v-if="column.dataIndex === 'status'">
            <a-tag v-if="record.status === 1" color="green">
              {{ statusMap[record.status as keyof typeof statusMap] as string }}
            </a-tag>
            <a-tag v-else color="orange">
              {{ statusMap[record.status as keyof typeof statusMap] as string }}
            </a-tag>
          </template>
        </template>
      </a-table>
    </a-card>
    <user-form-modal ref="userFormModal" @submit="handleSubmit" />
  </div>
</template>
<style lang="less" scoped></style>
