<?php
/**
 * Footer template
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }
?>
</main><!-- #site-content -->

<?php
$rendered_elementor_footer = false;
if ( function_exists( 'elementor_theme_do_location' ) ) {
    $rendered_elementor_footer = elementor_theme_do_location( 'footer' );
}

if ( ! $rendered_elementor_footer ) : ?>

    <footer id="colophon" class="w-full py-section-padding px-gutter flex flex-col items-center gap-stack-lg bg-primary text-on-primary">
        <div class="max-w-container-max w-full flex flex-col md:flex-row justify-between items-start gap-12 border-b border-on-primary/10 pb-12">
            <div class="flex flex-col gap-4 max-w-[300px]">
                <span class="font-h3 text-h3 font-bold text-on-primary"><?php bloginfo( 'name' ); ?></span>
                <p class="text-body-sm opacity-80"><?php bloginfo( 'description' ); ?></p>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-12">
                <?php if ( has_nav_menu( 'footer' ) ) : ?>
                    <div class="flex flex-col gap-4 col-span-2 md:col-span-3">
                        <h5 class="font-label-bold text-tertiary-fixed"><?php esc_html_e( 'Navigate', 'montenegrodrive' ); ?></h5>
                        <?php
                        wp_nav_menu(
                            array(
                                'theme_location'  => 'footer',
                                'container'       => false,
                                'menu_class'      => 'flex flex-wrap gap-6 list-none p-0 m-0 opacity-80 text-body-sm',
                                'depth'           => 1,
                            )
                        );
                        ?>
                    </div>
                <?php endif; ?>
            </div>
        </div>
        <div class="flex flex-col md:flex-row justify-between w-full max-w-container-max pt-2 opacity-70 text-body-sm">
            <p>
                <?php
                printf(
                    /* translators: 1: copyright year, 2: site name */
                    esc_html__( '© %1$s %2$s. All rights reserved.', 'montenegrodrive' ),
                    esc_html( date_i18n( 'Y' ) ),
                    esc_html( get_bloginfo( 'name' ) )
                );
                ?>
            </p>
        </div>
    </footer>

<?php endif; ?>

<?php wp_footer(); ?>
</body>
</html>
