import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# LINE CHART
# ==========================================================
def line_chart(df:pd.DataFrame,data_col:str,value_col:str,title:str,freq:str="ME"):
    data=(df.groupby(pd.Grouper(key=data_col,freq=freq))[value_col].sum().reset_index())
    fig=px.line(data,x=data_col,y=value_col,title=title,markers=True,template="plotly_white")
    fig.update_traces(line=dict(width=3),marker=dict(size=7))
    fig.update_layout(title_x=0.5,hovermode="x unified")
    return fig

# ==========================================================
# MULTI LINE CHART
# =========================================================
def multi_chart(df:pd.DataFrame,data_col:str,value_cols:list,title:str,freq:str="ME"):
    data=(df.groupby(pd.Grouper(key=data_col,freq=freq))[value_cols].sum().reset_index())
    fig=px.line(data,x=data_col,y=value_cols,title=title,markers=True)
    fig.update_traces(line=dict(width=3),marker=dict(size=6))
    fig.update_layout(title_x=0.5,hovermode="x unified")
    return fig

# ==========================================================
# BAR CHART
# ==========================================================
def bar_chart(df:pd.DataFrame,group_col:str,value_col:str|None,title:str,top_n:int=None,aggfunc:str="sum"):
   if value_col is None:
       data=(df.groupby(group_col).size().reset_index(name="value"))
       sort_col="value"
   else:
       if aggfunc=="sum":
            data=(df.groupby(group_col)[value_col].sum().reset_index())
       elif aggfunc=="mean":
            data=(df.groupby(group_col)[value_col].mean().reset_index())
       elif aggfunc=="count":
            data=(df.groupby(group_col)[value_col].nunique().reset_index())
       else:
            data=(df.groupby(group_col)[value_col].sum().reset_index())
       sort_col=value_col
   data = data.sort_values(
        sort_col,
        ascending=False
    )

   if top_n is not None:
        data = data.head(top_n)

   fig = px.bar(data,x=group_col,y=sort_col,title=title,text=sort_col,color=sort_col,color_continuous_scale=["#6A1B9A", "#D81B60", "#FF4081"])
   fig.update_traces(texttemplate="%{text:,0f}",textposition="outside",marker_line_width=2,marker_line_color="#FF2D7A")
   fig.update_layout(title_x=0.5,template="plotly_white",showlegend=False,xaxis_title=group_col,yaxis_title=sort_col,coloraxis_showscale=False)
#    fig = px.bar(
#         data,
#         x=group_col,
#         y=sort_col,
#         title=title,
#         text=sort_col,
#         color_discrete_sequence=["#E91E63"]
#     )

#    fig.update_traces(
#         texttemplate="%{text:,.0f}",
#         textposition="outside",
#         marker=dict(
#             color="#E91E63",
#             line=dict(width=0),
#             cornerradius=20
#         )
#     )

#    fig.update_layout(
#         title=dict(text=title, x=0.5),
#         template="plotly_white",
#         showlegend=False,
#         plot_bgcolor="#F5A1C4",
#         paper_bgcolor="#F5A1C4",
#         xaxis=dict(showgrid=False, title=""),
#         yaxis=dict(showgrid=False, title="", visible=False),
#         margin=dict(l=20, r=20, t=60, b=20)
#     )

#    return fig




     

#    fig = px.bar(data,x=group_col,y=sort_col,title=title,text=sort_col)
#    fig.update_traces(texttemplate="%{text:,0f}",textposition="outside",marker_line_width=2,marker_line_color="#FF2D7A")
#    fig.update_layout(title_x=0.5,template="plotly_white",showlegend=False,xaxis_title=group_col,yaxis_title=sort_col,coloraxis_showscale=False)


   return fig    

# ==========================================================
# HORIZONTAL BAR CHART
# ==========================================================
def horizontal_bar_chart(df: pd.DataFrame,group_col: str,value_col: str,title: str,top_n: int = None):

    data = (
        df.groupby(group_col)[value_col]
        .sum()
        .reset_index()
    )

    data = data.sort_values(
        value_col,
        ascending=True
    )

    if top_n is not None:
        data = data.tail(top_n)

    fig = px.bar(data,y=group_col,x=value_col,orientation="h",title=title)
    fig.update_traces(textposition="outside",texttemplate="%{text}")
    fig.update_layout(title_x=0.5, xaxis_title=value_col,yaxis_title=group_col)

    return fig


# ==========================================================
# PIE CHART
# ==========================================================

def pie_chart(
    df: pd.DataFrame,
    names_col: str,
    title: str
):

    data = (df[names_col].value_counts() .reset_index())

    data.columns = [names_col,"Count"]

    fig = px.pie(data,names=names_col, values="Count",title=title,color_discrete_sequence=[
            "#4361EE", "#7209B7", "#F72585",
            "#FF9F1C", "#2EC4B6", "#4CC9F0"])
    fig.update_traces(
        textinfo="percent+label",
        textposition="outside",
        pull=[0.03] * len(data),
        marker=dict(line=dict(color="white", width=3))
    )

    fig.update_layout(
        title_x=0.5,
        template="plotly_white",
        showlegend=False
    )


    return fig

# ==========================================================
# DONUT CHART
# ==========================================================
def donut_chart(df: pd.DataFrame, names_col: str,title: str):

    data = (df[names_col].value_counts().reset_index())

    data.columns = [names_col,"Count"]

    fig = px.pie(data,names=names_col,values="Count",hole=0.5,title=title,
        color_discrete_sequence=["#4361EE", "#7209B7", "#F72585", "#FF9F1C", "#2EC4B6"]
    )

    fig.update_traces(textinfo="percent+label",textposition="outside",marker=dict(line=dict(color="white", width=2)))

    fig.update_layout(title_x=0.5, template="plotly_white", showlegend=False)

    return fig

# ==========================================================
# HISTOGRAM
# ==========================================================
def histogram(
    df: pd.DataFrame,
    column: str,
    title: str,
    bins: int = 30
):

    fig = px.histogram(
        df,
        x=column,
        nbins=bins,
        title=title,color_discrete_sequence=["#00B4D8"]
    )

    fig.update_traces(marker_line_color="#0077B6",marker_line_width=2,opacity=0.9)
    fig.update_layout(
        title_x=0.5,
        template="plotly_white",
        xaxis_title=column,
        yaxis_title="Count"
    )

    return fig


# ==========================================================
# SCATTER CHART
# ==========================================================
def scatter_chart(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: str | None,
    title: str
):

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col,
        title=title,
        hover_data=df.columns,
        template="plotly_white",
        opacity=0.65
    )

    fig.update_traces( marker=dict(size=8,line=dict(width=1)))
    fig.update_layout(title_x=0.5,xaxis_title=x_col,yaxis_title=y_col,hovermode="closest")

    return fig
    return fig

# ==========================================================
# BOX PLOT
# ==========================================================

def box_plot(
    df: pd.DataFrame,
    y_col: str,
    x_col: str | None,
    title: str
):

    fig = px.box(
        df,
        y=y_col,
        x=x_col,
        title=title,
        template="plotly_white",
        points="outliers"
    )

    fig.update_traces(
        marker=dict(size=5),
        line=dict(width=2)
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title=x_col,
        yaxis_title=y_col
    )

    return fig


# ==========================================================
# VIOLIN PLOT
# ==========================================================
def violin_plot(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str
):

    fig = px.violin(
        df,
        x=x_col,
        y=y_col,
        box=True,
        title=title
    )

    return fig

# ==========================================================
# HEATMAP
# ==========================================================

def heatmap(
    data: pd.DataFrame,
    title: str
):

    fig = go.Figure(
        data=go.Heatmap(
            z=data.values,
            x=data.columns,
            y=data.index,
            text=data.round(2).values,
            texttemplate="%{text}",
            colorscale="RdBu_r",
            zmid=0
        )
    )

    fig.update_layout(title=title,title_x=0.5,template="plotly_white")

    return fig

# ==========================================================
# CORRELATION HEATMAP
# ==========================================================
def correlation_heatmap(
    df: pd.DataFrame,
    columns: list,
    title: str
):

    corr_matrix = df[columns].corr()

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        z_min=-1,
        z_max=1,
        zmid=0,
        title=title
    )

    fig.update_layout(title=title,title_x=0.5,template="plotly_white")

    return fig


# ==========================================================
# WATERFALL CHART
# ==========================================================
def waterfall_chart(
    df: pd.DataFrame,
    category_col: str,
    value_col: str,
    title: str
):

    data = (
        df.groupby(category_col)[value_col]
        .sum()
        .reset_index()
    )

    fig = go.Figure(
        go.Waterfall(
            x=data[category_col],
            y=data[value_col],
            textposition="outside",
            text=data[value_col],
            connector={"line": {"width": 1}}
        )
    )

    fig.update_layout(title=title,title_x=0.5,template="plotly_white",showlegend=False)

    return fig
# ==========================================================
# DEFAULT RATE CHART
# ==========================================================
def default_rate_chart(
    df: pd.DataFrame,
    group_col: str,
    title: str
):

    data = (
        df.groupby(group_col)["TARGET"]
        .mean()
        .reset_index(name="Default Rate %")
    )

    data["Default Rate %"] = (
        data["TARGET"] * 100
    )

    fig = px.bar(
        data,
        x=group_col,
        y="Default Rate %",
        color="Default Rate %",
        color_continuous_scale="RdYlGn_r",
        text="Default Rate %",
        title=title
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        title_x=0.5,
        template="plotly_white",
        yaxis_title="Default Rate (%)",
        coloraxis_colorbar_title="Default %"
    )

    return fig

# ==========================================================
# MISSING VALUE CHART
# ==========================================================

def missing_values_chart(
    df: pd.DataFrame,
    top_n: int = 20
):

    missing = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    fig = px.bar(
        x=missing.index,
        y=missing.values,
        title="Top Missing Value Columns",
         template="plotly_white"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title="Missing Values",
        yaxis_title="Columns"
    )

    return fig


# ==========================================================
# RISK GAUGE CHART
# ==========================================================
def risk_gauge(
    score: float,
    title: str = "Risk Score"
):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={"text": title},
            number={"suffix":"%"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
                "steps":[
                    {"range": [0, 40], "color": "lightgreen"},
                    {"range": [40, 70], "color": "gold"},
                    {"range": [70, 100], "color": "lightcoral"}
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "value": score
                }
            }
        )
    )

    fig.update_layout(
        title_x=0.5,
        template="plotly_white"
    )

    return fig

# ==========================================================
# Risk Quadrant.
# ==========================================================
def credit_risk_quadrant(
    df: pd.DataFrame,
    income_col: str = "AMT_INCOME_TOTAL",
    credit_col: str = "AMT_CREDIT",
    target_col: str = "TARGET",
    title: str = "Credit Risk Quadrant"
):

    data = df[
        [income_col, credit_col, target_col]
    ].dropna().copy()

    data["Risk Status"] = data[target_col].map({
        0: "Non-Default",
        1: "Default"
    })

    # Median lines
    income_median = data[income_col].median()
    credit_median = data[credit_col].median()

    # Remove extreme values only for visualization
    income_limit = data[income_col].quantile(0.99)
    credit_limit = data[credit_col].quantile(0.99)

    plot_data = data[
        (data[income_col] <= income_limit) &
        (data[credit_col] <= credit_limit)
    ]

    # Limit points for faster rendering
    if len(plot_data) > 10000:
        plot_data = plot_data.sample(
            10000,
            random_state=42
        )

    fig = px.scatter(
        plot_data,
        x=income_col,
        y=credit_col,
        color="Risk Status",
        title=title,
        opacity=0.65,
        hover_data=[target_col]
    )

    fig.add_vline(
        x=income_median,
        line_dash="dash",
        annotation_text="Median Income"
    )

    fig.add_hline(
        y=credit_median,
        line_dash="dash",
        annotation_text="Median Credit"
    )

    fig.update_layout(
        title_x=0.5,
        xaxis_title="Total Income",
        yaxis_title="Credit Amount",
        legend_title="Customer Status",
        template="plotly_white"
    )

    return fig

# ------------------------------------------------------
    # 3D Globe Chart
    # ------------------------------------------------------

def home_credit_3d_globe(
    df: pd.DataFrame,
    credit_col: str = "AMT_CREDIT",
    income_col: str = "AMT_INCOME_TOTAL",
    annuity_col: str = "AMT_ANNUITY",
    id_col: str = "SK_ID_CURR",
    title: str = "Home Credit 3D Globe",
    max_points: int = 1500
):

    data = df.copy()

    # ------------------------------------------------------
    # Check required columns
    # ------------------------------------------------------

    required_cols = [
        credit_col,
        income_col,
        annuity_col
    ]

    for col in required_cols:
        if col not in data.columns:
            raise ValueError(
                f"Column '{col}' not found in dataframe."
            )

    # ------------------------------------------------------
    # Keep ID if available
    # ------------------------------------------------------

    if id_col not in data.columns:
        data[id_col] = range(1, len(data) + 1)

    # ------------------------------------------------------
    # Remove missing values
    # ------------------------------------------------------

    data = data.dropna(
        subset=[
            credit_col,
            income_col,
            annuity_col
        ]
    )

    # ------------------------------------------------------
    # Remove invalid values
    # ------------------------------------------------------

    data = data[
        (data[credit_col] >= 0) &
        (data[income_col] >= 0) &
        (data[annuity_col] >= 0)
    ]

    # ------------------------------------------------------
    # Limit number of points
    # ------------------------------------------------------

    if len(data) > max_points:

        data = data.sample(
            max_points,
            random_state=42
        )

    data = data.reset_index(drop=True)

    # ------------------------------------------------------
    # Normalize financial values
    # ------------------------------------------------------

    def normalize(series):

        min_val = series.min()
        max_val = series.max()

        if max_val == min_val:
            return pd.Series(
                [0.5] * len(series),
                index=series.index
            )

        return (
            (series - min_val)
            / (max_val - min_val)
        )

    credit_norm = normalize(data[credit_col])

    income_norm = normalize(data[income_col])

    annuity_norm = normalize(data[annuity_col])

    # ------------------------------------------------------
    # Convert financial values into spherical coordinates
    # ------------------------------------------------------
    #
    # This creates the "globe" effect.
    #
    # Income  -> latitude
    # Credit  -> longitude
    # Annuity -> distance from globe center
    #
    # ------------------------------------------------------

    longitude = (
        credit_norm * 2 * 3.14159265359
        - 3.14159265359
    )

    latitude = (
        income_norm * 3.14159265359
        - (3.14159265359 / 2)
    )

    radius = (
        1.02 +
        annuity_norm * 0.12
    )

    # ------------------------------------------------------
    # Convert spherical coordinates to XYZ
    # ------------------------------------------------------

    x = (
        radius
        * __import__("numpy").cos(latitude)
        * __import__("numpy").cos(longitude)
    )

    y = (
        radius
        * __import__("numpy").cos(latitude)
        * __import__("numpy").sin(longitude)
    )

    z = (
        radius
        * __import__("numpy").sin(latitude)
    )

    # ------------------------------------------------------
    # Create globe surface
    # ------------------------------------------------------

    import numpy as np

    phi = np.linspace(
        0,
        np.pi,
        40
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        80
    )

    globe_x = (
        np.outer(
            np.sin(phi),
            np.cos(theta)
        )
    )

    globe_y = (
        np.outer(
            np.sin(phi),
            np.sin(theta)
        )
    )

    globe_z = (
        np.outer(
            np.cos(phi),
            np.ones(len(theta))
        )
    )

    # ------------------------------------------------------
    # Create figure
    # ------------------------------------------------------

    fig = go.Figure()

    # ------------------------------------------------------
    # Globe
    # ------------------------------------------------------

    fig.add_trace(
        go.Surface(

            x=globe_x,
            y=globe_y,
            z=globe_z,

            colorscale=[
                [0, "#4A148C"],
                [0.35, "#7B1FA2"],
                [0.65, "#E91E63"],
                [1, "#F8BBD0"]
            ],

            opacity=0.28,

            showscale=False,

            hoverinfo="skip"
        )
    )

    # ------------------------------------------------------
    # Financial points
    # ------------------------------------------------------

    fig.add_trace(
        go.Scatter3d(

            x=x,
            y=y,
            z=z,

            mode="markers",

            marker=dict(

                size=5,

                color=data[income_col],

                colorscale=[
                    [0.00, "#4A148C"],
                    [0.25, "#7B1FA2"],
                    [0.50, "#E91E63"],
                    [0.75, "#F06292"],
                    [1.00, "#FFCDD2"]
                ],

                opacity=0.9,

                line=dict(
                    color="#FFFFFF",
                    width=0.5
                ),

                colorbar=dict(
                    title="Income",
                    thickness=15
                )
            ),

            customdata=data[
                [
                    id_col,
                    credit_col,
                    income_col,
                    annuity_col
                ]
            ],

            hovertemplate=(
                "<b>💳 Application</b><br><br>"
                "ID: %{customdata[0]}<br>"
                "Credit: ₹%{customdata[1]:,.0f}<br>"
                "Income: ₹%{customdata[2]:,.0f}<br>"
                "Annuity: ₹%{customdata[3]:,.0f}"
                "<extra></extra>"
            )
        )
    )

    # ------------------------------------------------------
    # Layout
    # ------------------------------------------------------

    fig.update_layout(

        title=dict(
            text="🌐 " + title,
            x=0.5,

            font=dict(
                size=25,
                color="#6A1B9A"
            )
        ),

        template="plotly_white",

        paper_bgcolor="#FDF2F8",

        scene=dict(

            bgcolor="#FDF2F8",

            xaxis=dict(
                visible=False
            ),

            yaxis=dict(
                visible=False
            ),

            zaxis=dict(
                visible=False
            ),

            aspectmode="cube",

            camera=dict(
                eye=dict(
                    x=1.6,
                    y=1.6,
                    z=1.2
                )
            )
        ),

        margin=dict(
            l=0,
            r=0,
            t=70,
            b=0
        ),

        showlegend=False
    )

    return fig


            
