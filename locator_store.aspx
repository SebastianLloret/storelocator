<%@ page language="VB" masterpagefile="~/elope_solid.master" autoeventwireup="false" inherits="store_locator, App_Web_locator_store.aspx.cdcab7d2" title="Locate a store near you that sells elope hats, glasses and other zany costume merchandise from this search page. Elope manufactures, sells fun, costume & licensed hats, glasses, accessories to retailers nationwide." %>
    <asp:Content ID="Content1" ContentPlaceHolderID="ContentProductCategories" Runat="Server">
    </asp:Content>
    <asp:Content ID="Content2" ContentPlaceHolderID="contentMain" Runat="Server">
        <table border="0" cellspacing="0" cellpadding="0" width="100%" height="100%" class="static_white_background">

            <tr>
                <td class="background_static_tl"></td>
                <td style="width: 490px;"></td>
                <td class="background_static_tr"></td>
            </tr>

            <tr>
                <td colspan="3" class="templateBodyStatic">
                    <div style="padding-bottom: 8px; text-align: center;">
                        <div class="title"> <img src="layout_images/estore_heading.gif" alt="arrow" align="absmiddle" /> Find Store Locations in USA <img src="layout_images/estore_heading.gif" alt="arrow" align="absmiddle" />
                        </div>
                        enter your zip code below</div>

                    <div style="padding-bottom: 12px; padding-top: 6px;">
                        <p>Looking for our hats, glasses & other merchandise? Just enter you zip code below and find out which stores near you sell our wares.
                        </p>
                        <p><a href="http://www.elope.com/locator_store_canada.aspx" target="_self">Click Here to View Store Locations in Canada</a>
                        </p>
                    </div>

                    <div class="estore_title">Zip Code</div>

                    <table cellspacing="0" style="padding:0px 0px 0px 0px;border:none 0px white;">
                        <tr>
                            <td style="vertical-align:middle;">
                                <asp:TextBox ID="txtZip" CssClass="textbox" Columns="10" runat="server"></asp:TextBox>
                            </td>

                            <td style="vertical-align:middle;">
                                <asp:Button ID="btnZipCode" runat="server" Text="" Style="border-width:0px;border-style:none;background-image:url(layout_images/btn_find_store.gif);width:74px;height:26px;" />
                            </td>
                        </tr>
                    </table>

                    <div style="padding-top: 8px;">
                        <asp:Label ID="lblZipMessage" runat="server"></asp:Label>
                    </div>

                    <div style="text-align: center">
                        <asp:datalist id="dlStores" runat="server" CellSpacing="6" cellpadding="3" repeatcolumns="2" horizontalalign="NotSet" ItemStyle-VerticalAlign="Top" RepeatDirection="Vertical">

                            <ItemStyle HorizontalAlign="left" VerticalAlign="Top"></ItemStyle>

                            <ItemTemplate>
                                <div>
                                    <table cellpadding="3" cellspacing="3" border="0" style="width: 200px; border: 1px dotted #a9a9a9; height: 125px;">
                                        <tr>
                                            <td valign="top">
                                                <div style="padding-bottom: 1px;" class="estore_title">
                                                    <%#DataBinder.Eval(Container.DataItem, "Store")%>
                                                </div>

                                                <div>
                                                    <%#DataBinder.Eval(Container.DataItem, "Address1")%>
                                                </div>

                                                <div>
                                                    <%#DataBinder.Eval(Container.DataItem, "Address2")%>
                                                </div>

                                                <div>
                                                    <%#DataBinder.Eval(Container.DataItem, "Address3")%>
                                                </div>

                                                <div>
                                                    <%#DataBinder.Eval(Container.DataItem, "City")%>,
                                                        <%#DataBinder.Eval(Container.DataItem, "State")%>
                                                            <%#DataBinder.Eval(Container.DataItem, "Zip")%>
                                                </div>

                                                <div style="padding-bottom: 5px; padding-top: 8px;">
                                                    <%#IIf(DataBinder.Eval(Container.DataItem, "Phone") Is DBNull.Value, "<br>", "<img src=layout_images/phone1.gif align=absmiddle  /> " & DataBinder.Eval(Container.DataItem, "Phone"))%>
                                                </div>

                                                <div style="padding-bottom: 4px;">
                                                    <%#IIf(DataBinder.Eval(Container.DataItem, "Website") Is DBNull.Value, "<br>", "<a class=" "b2blink" " target=" "_blank" " href=" "http://" & DataBinder.Eval(Container.DataItem, "Website") & "" ">" & DataBinder.Eval(Container.DataItem, "Website") & "</a>")%>
                                                </div>

                                            </td>
                                        </tr>
                                    </table>
                                </div>

                            </ItemTemplate>
                        </asp:datalist>
                    </div>
                </td>
            </tr>

            <tr>
                <td class="background_static_bl"></td>
                <td style="width: 490px;"></td>
                <td class="background_static_br"></td>
            </tr>
            
        </table>
    </asp:Content>
