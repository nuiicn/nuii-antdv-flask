<script setup lang="ts">
import type { UnwrapRef } from 'vue'
import type { TreeSelectProps } from 'ant-design-vue'
import { TreeSelect } from 'ant-design-vue'
import { CheckOutlined, EditOutlined } from "@ant-design/icons-vue"
import { cloneDeep } from "lodash-es"
import {
  UserTableModel,
  UserTableColumn,
  UpdateTableColumn,
  updateUserTableColumnApi
} from '@/api/customize/system/user.ts'
import { getDepartmentTreeApi } from '@/api/customize/system/department.ts'

const props = defineProps<{
  dataSource: UserTableModel[]
  record: UserTableModel
  column: UserTableColumn
}>()

const editableColumn: UnwrapRef<Record<string, UserTableModel | any>> = reactive({})
const selectedColumn = ref()
const SHOW_ALL = TreeSelect.SHOW_ALL
const treeData = ref<TreeSelectProps['treeData']>()
const selectedTree = ref<string>('')

const getDepartmentTree = async () => {
  try {
    const { data } = await getDepartmentTreeApi()
    treeData.value = data
  }
  catch (e) {
    console.log(e)
  }
}

const updateUserTableColumn = async (id: string, column: string, value: string, type: string) => {
  try {
    const params: UpdateTableColumn = {
      'id': id,
      'column': column,
      'value': value,
      'type': type,
    }
    const { code, data } = await updateUserTableColumnApi(params)
    if (code === 200) {
      Object.assign(props.dataSource.filter(item => id === item.id)[0], data)
      selectedColumn.value = ''
      delete editableColumn[id]
    }
  }
  catch (e) {
    console.log(e)
  }
}

const editableColumnEdit = async (id: string, column: string) => {
  await getDepartmentTree()
  editableColumn[id] = cloneDeep(props.dataSource.filter(item => id === item.id)[0])
  selectedColumn.value = column
  selectedTree.value = editableColumn[id][column][0].id
}

const editableColumnSave = async (id: string, column: string, selectedTree: string, type: string) => {
  await updateUserTableColumn(id, column, selectedTree, type)
}
</script>
<template>
  <div class="editable-cell">
    <div v-if="editableColumn[record.id] && selectedColumn === column.dataIndex">
      <a-tree-select
        v-model:value="selectedTree"
        class="editable-cell-select"
        tree-node-filter-prop="title"
        :show-checked-strategy="SHOW_ALL"
        tree-default-expand-all
        :tree-data="treeData"
        :tree-line="true"
        style="min-width: 150px"
      />
      <check-outlined
          class="editable-cell-icon-check"
          @click="editableColumnSave(record.id, selectedColumn, selectedTree, 'tree')"
      />
    </div>
    <div v-else>
      <a-tag color="green">
        <span v-for="(item, index) in record.department_id" :key="index">
          <span>{{ item.name }}</span>
          <span v-if="index < record.department_id.length - 1"> - </span>
        </span>
      </a-tag>
      <edit-outlined
        class="editable-cell-icon"
        @click="editableColumnEdit(record.id, column.dataIndex)"
      />
    </div>
  </div>
</template>
