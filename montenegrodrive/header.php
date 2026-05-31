<?php
/**
 * Header template
 *
 * If Elementor Pro Theme Builder has a "header" location set, we let it handle
 * the entire header markup. Otherwise we render a sensible fallback so the site
 * still has navigation before any Elementor templates are imported.
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }
?><!DOCTYPE html>
<html <?php language_attributes(); ?> class="light">
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <?php wp_head(); ?>
</head>
<body <?php body_class( 'bg-background text-on-background font-body-md antialiased' ); ?>>
<?php wp_body_open(); ?>

<a class="skip-link screen-reader-text" href="#site-content"><?php esc_html_e( 'Skip to content', 'montenegrodrive' ); ?></a>

<?php
/* ----------------------------------------------------------- *
 *  If Elementor Pro is rendering a custom header, defer to it.
 * ----------------------------------------------------------- */
$rendered_elementor_header = false;
if ( function_exists( 'elementor_theme_do_location' ) ) {
    $rendered_elementor_header = elementor_theme_do_location( 'header' );
}

if ( ! $rendered_elementor_header ) : ?>

    <header id="masthead" class="fixed top-0 w-full z-50 bg-surface shadow-sm">
        <div class="max-w-container-max mx-auto flex justify-between items-center px-gutter py-4">
            <div class="flex items-center gap-10">
                <?php if ( has_custom_logo() ) : ?>
                    <div class="site-logo"><?php the_custom_logo(); ?></div>
                <?php else : ?>
                    <a class="font-h2 text-h2 font-bold text-primary" href="<?php echo esc_url( home_url( '/' ) ); ?>">
                        <?php bloginfo( 'name' ); ?>
                    </a>
                <?php endif; ?>

                <nav class="hidden md:flex gap-6" aria-label="<?php esc_attr_e( 'Primary navigation', 'montenegrodrive' ); ?>">
                    <?php
                    if ( has_nav_menu( 'primary' ) ) {
                        wp_nav_menu(
                            array(
                                'theme_location'  => 'primary',
                                'container'       => false,
                                'menu_class'      => 'flex gap-6 list-none p-0 m-0',
                                'fallback_cb'     => false,
                                'depth'           => 1,
                                'link_before'     => '',
                                'link_after'      => '',
                            )
                        );
                    } else {
                        echo '<span class="text-secondary text-body-sm italic">' . esc_html__( 'Assign a menu in Appearance → Menus.', 'montenegrodrive' ) . '</span>';
                    }
                    ?>
                </nav>
            </div>
            <div class="flex items-center gap-4">
                <button class="hidden md:block text-secondary font-label-bold hover:text-primary transition-colors">
                    <?php esc_html_e( 'Support', 'montenegrodrive' ); ?>
                </button>
                <a class="bg-primary text-on-primary px-6 py-2.5 rounded-lg font-label-bold hover:shadow-lg transition-all"
                   href="<?php echo esc_url( home_url( '/manage-booking/' ) ); ?>">
                    <?php esc_html_e( 'Manage Booking', 'montenegrodrive' ); ?>
                </a>
            </div>
        </div>
    </header>

<?php endif; ?>

<main id="site-content" class="<?php echo $rendered_elementor_header ? '' : 'pt-[72px]'; ?>">
