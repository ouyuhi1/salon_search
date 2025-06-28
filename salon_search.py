{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "30385a1b-23ba-443a-8d19-c2aadeac6d04",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import streamlit as st\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1923cb40-2295-4645-a967-d5093fc6fda7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# merged.csvを読み込む\n",
    "merged_df = pd.read_csv(\"merged.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a05333c6-d814-44be-ac7a-58fd028eab2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 11:54:37.659 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.659 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.661 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.663 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.665 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.666 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.667 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:37.668 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# streamlitの部品設計\n",
    "st.title(\"サロンサーチ\")\n",
    "\n",
    "# フィルタ設定\n",
    "price_limit = st.slider(\"最低カット価格の上限\", min_value=2000, max_value=8500, step=200, value=6000)\n",
    "score_limit = st.slider(\"人気スコアの下限\", min_value=0.0, max_value=35.0, step=2.0, value=5.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5c0b8484-9cc3-4b96-a568-86b9018e7b62",
   "metadata": {},
   "outputs": [],
   "source": [
    "# フィルタ処理\n",
    "filtered_df = merged_df[\n",
    "    (merged_df['price'] <= price_limit) &\n",
    "    (merged_df['pop_score'] >= score_limit)\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ed1ad43d-baee-45de-80c9-87b5aa4d9416",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 11:53:34.378 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:34.378 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:34.378 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:34.378 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:34.378 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 散布図の作成（人気スコア x 最低カット価格）\n",
    "fig = px.scatter(\n",
    "    filtered_df,\n",
    "    x='pop_score',\n",
    "    y='price',\n",
    "    hover_data=['name_salon', 'access', 'star'],\n",
    "    title='人気スコアと最低カット価格の散布図'\n",
    ")\n",
    "\n",
    "st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "4aca3389-fd46-49f3-b4d4-89d0681d0ebe",
   "metadata": {
    "jupyter": {
     "source_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 11:53:45.065 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:45.091 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:45.099 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:45.110 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:53:45.112 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 散布図の作成（人気スコア x 最低カット価格）\n",
    "fig = px.scatter(\n",
    "    filtered_df,\n",
    "    x='pop_score',\n",
    "    y='price',\n",
    "    hover_data=['name_salon', 'access', 'star'],\n",
    "    title='人気スコアと最低カット価格の散布図'\n",
    ")\n",
    "\n",
    "st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9cf527a9-e7ac-4dc0-835c-9de5eedbe2e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 11:54:23.069 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:23.076 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:23.076 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:23.076 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:54:23.076 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 散布図の作成（人気スコア x 最低カット価格）\n",
    "fig = px.scatter(\n",
    "    filtered_df,\n",
    "    x='pop_score',\n",
    "    y='price',\n",
    "    hover_data=['name_salon', 'access', 'star'],\n",
    "    title='人気スコアと最低カット価格の散布図'\n",
    ")\n",
    "\n",
    "st.plotly_chart(fig)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9ce8ccc6-66d6-4316-b183-5e727ac58742",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 11:56:06.665 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.666 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.666 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.666 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.669 Session state does not function when running a script without `streamlit run`\n",
      "2025-06-22 11:56:06.670 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.670 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.671 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.673 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.676 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 11:56:06.676 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# 詳細リンクの表示\n",
    "selected_salon = st.selectbox('気になるサロンを選んで詳細を確認', filtered_df['name_salon'])\n",
    "\n",
    "if selected_salon:\n",
    "    url = filtered_df[filtered_df['name_salon'] == selected_salon]['link_detail'].values[0]\n",
    "    st.markdown(f\"[{selected_salon}のページへ移動]({url})\", unsafe_allow_html=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "bf8e359b-5ecd-47a2-ad81-92554b6fea2f",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 12:06:25.456 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:25.456 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:25.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:25.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:25.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:25.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:25.460 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "sort_key = st.selectbox(\n",
    "    \"ランキング基準を選んでください\",\n",
    "    (\"star\", \"pop_score\", \"review\", \"price\", \"seats\")\n",
    ")\n",
    "\n",
    "ascending = True if sort_key == \"price\" else False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "71d3ed35-ed69-4885-8891-6799c8935710",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 12:06:39.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:39.907 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:39.909 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:39.946 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:39.946 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-22 12:06:39.950 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.subheader(f\"{sort_key}によるサロンランキング（上位10件）\")\n",
    "\n",
    "ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)\n",
    "\n",
    "# 必要な列だけ表示\n",
    "st.dataframe(ranking_df[[\"name_salon\", \"price\", \"pop_score\", \"star\", \"review\", \"seats\", \"access\"]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a578f96-ed4e-44f2-8f95-43c81e3e59ed",
   "metadata": {
    "editable": true,
    "slideshow": {
     "slide_type": ""
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
