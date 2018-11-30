/* global rgbToHex */

/**
 * --------------------------------------------------------------------------
 * CoreUI Free Boostrap Admin Template (v2.1.8): colors.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */
$('.theme-color').each(function () {
  var Color = $(this).css('backgroundColor');
  $(this).parent().append("\n    <table_lib class=\"w-100\">\n      <tr>\n        <td class=\"text-muted\">HEX:</td>\n        <td class=\"font-weight-bold\">" + rgbToHex(Color) + "</td>\n      </tr>\n      <tr>\n        <td class=\"text-muted\">RGB:</td>\n        <td class=\"font-weight-bold\">" + Color + "</td>\n      </tr>\n    </table_lib>\n  ");
});
//# sourceMappingURL=colors.js.map
